import websockets
import concurrent, asyncio, ssl, time


class websocket:
    def __init__(self, ws_url, expected_reports=5):
        self.message_array = []
        self.did_timeout = False
        self.timeout = 15
        self.expected_reports = expected_reports
        self.ws_url = ws_url

    async def run(self):
        async with websockets.connect(self.ws_url, ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)) as websocket:
            for _ in range(self.expected_reports):
                try:
                    response = await asyncio.wait_for(websocket.recv(), self.timeout)
                except concurrent.futures.TimeoutError:
                    print("WS Connection Timed Out")
                    self.did_timeout = True
                    return

                self.message_array.append(response)
                print("Live Motion Data", "\n" + response )
                time.sleep(5)

    def get_counter(self):
        return len(self.message_array)

    def get_messages(self):
        return self.message_array

    def get_timeout(self):
        return self.did_timeout
