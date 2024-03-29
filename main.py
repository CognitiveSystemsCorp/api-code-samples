import requests, threading, asyncio, pprint
from lib.websocket_utils import websocket

CLOUD_SPACE = "dummy.cloud.url" ## Replace this value with the correct cloud space value for accessing your system 

def main():
    email = "dummy@gmail.com" ## Replace this value with credentials you have for evaluation kit
    password = "Dummy12345!@#" ## Replace this value with credentials you have for evaluation kit
    URL = "https://" + CLOUD_SPACE

    try:
        #POST API = Login and Begin Session
        #RESPONSE:  
        # /"refresh_token"
        # /"token"                                                      ##system generates new token on every call of this api
        # /"user": {
        #           "id"
        #           "email"
        #           "confirmed_at"
        #           "first_name"
        #           "last_name"
        #           "created_at"
        #           "updated_at"
        #          }
        response = requests.post(
            URL + "/sessions",
            data = {"email": email, "password": password}) #Request body
        data = response.json()
        token_str = data["token"]
        print("Token",token_str)

        # We are going to attach the token as header in each api call further
        header = {"Authorization": token_str} 


        #GET API = GET GENERAL SETTINGS
        #RESPONSE:  
        # /{data}
        # {
        #     "data": [
        #         {
        #             "id"
        #             "name"
        #             "created_at"
        #             "updated_at"
        #             "external_id"          
        #             "user_count"
        #             "latitude"
        #             "longitude"
        #             "address"
        #             "timezone"
        #             "pet_size"                                        ## Denotes if the user has pet, amd if yes then of what size // Values: none, small, medium, large
        #             "building_type"
        #             "building_size"
        #             "live_enabled"
        #             "subscription_id"
        #             "scene_id"                                        ## Represents network home/away mode: 4 = home mode, 1 = Away mode
        #             "network_scene_config"                            ## To be used later as network scene config id to show and update scene settings
        #             "owner_email"
        #             "present_count"
        #             "claimed"
        #         }
        #     ]
        # }
        response = requests.get(
            URL + "/networks",
            headers = header)
        general_settings_data = response.json()
        id =  str(general_settings_data["data"][0]["id"])
        hasPet = str(general_settings_data["data"][0]["pet_size"])
        network_scene_config_id = str(general_settings_data["data"][0]["network_scene_config"])  
        #print("network_scene_config_id",network_scene_config_id)
        #print("pet_size",hasPet)



        # PUT API = UPDATE GENERAL SETTINGS
        #RESPONSE
        # /{data}
        # {
        #     "data": [
        #         {
        #             "id"
        #             "name"
        #             "created_at"
        #             "updated_at"
        #             "external_id"         
        #             "user_count"
        #             "latitude"
        #             "longitude"
        #             "address"
        #             "timezone"
        #             "pet_size"             
        #             "building_type"
        #             "building_size"
        #             "live_enabled"
        #             "subscription_id"
        #             "scene_id"                                        ## To change home/away mode, change the value to: 4 or 1, where 4 = home mode, 1 = Away mode
        #             "network_scene_config"
        #             "owner_email"
        #             "present_count"
        #             "claimed"
        #         }
        #     ]
        # } 
        response = requests.put(
            URL + "/networks/" + id,
            data =  {
                "id": str(general_settings_data["data"][0]["id"]),
                "name": str(general_settings_data["data"][0]["name"]),
                "latitude": str(general_settings_data["data"][0]["latitude"]),
                "longitude": str(general_settings_data["data"][0]["longitude"]),
                "address": str(general_settings_data["data"][0]["address"]),
                "timezone": str(general_settings_data["data"][0]["timezone"]),
                "pet_size": str(general_settings_data["data"][0]["pet_size"]),
                "building_type": str(general_settings_data["data"][0]["building_type"]),
                "building_size": str(general_settings_data["data"][0]["building_size"]),
                "live_enabled": general_settings_data["data"][0]["live_enabled"],
                "scene_id": 4,
            },                                        ## REQUEST BODY
            headers = header)
        data = response.json()
        #print("pet_size",data["pet_size"])



        #GET API = MOTION HISTORY DENSITIES
        #RESPONSE:
        #[
            # [
            #     0.826388888888889,                                   ## Motion Intensity 
            #     1637028000                                           ## TimeStamp when motion of above intensity occured
            # ], ...
        #]
        UTC_TIME_NOW = "1637546100"
        UTC_TIME_01_NOV = "1635731700"

        response = requests.get(
            URL + "/motion_history_densities" 
            #+ "?from="+ UTC_TIME_01_NOV +"&to="+ UTC_TIME_NOW         ## QueryString variables used are optional
            ,headers = header)
        data = response.json()
        #print("Motion History Data",str(data))                        ## Prints an array list of intesities of motion with timestamp when motion occured 
        


############################################# SOUNDING V2 API ##########################################################


    #GET API = GET GLOBAL SETTINGS
        #RESPONSE:
        # {
        #     "motion_events_enabled": 1,                               #Enable/Disable the Home/Away mode of network
        #     "motion_events_armed": 1,                                 #Enable/Disable logging of MotionDetectedEvents in cloud history
        #     "mesh_auto_disable": 0,                                   #Enable/Disable mesh link sounding on all current and future nodes.     
        #     "sounding_mode": "allow",                                 #Enable/Disable sounding state of the network
        #     "leafblower_cutoff": 0,                                   #Minimum score for leafblower to sound a client device
        #     "zone_priority_list": [                                   #List of zones in prioritized order
        #         "Router",
        #         "Bhumik room",
        #         "Aidan room",
        #         "Glass"
        #     ],
        #     "sensitivity": 1,                                         #Motion Detection Sensitivity (1.0 - high, 2.0 - medium, 3.0 - low, generally bigger => less motion)
        #     "pet_mode": 0,                                            #Enable/Disable the pet filtering
        #     "cooldown": 120                                           #Minimum period between successive MotionDetectedEvent (sec)
        # }
        response = requests.get(
            URL + "/sounding/settings/",
            headers = header)                                           
        data = response.json()
        print("GET GLOBAL SETTINGS")
        pprint.pprint(data)


    #GET API = GET CLIENT STATE
        #RESPONSE:
        # {
        #     "devices": [
        #         {
        #             "is_node": true,                                  #Denotes if the given device is node or a leaf
        #             "is_extender": false,                             #Denotes if device is master or slave node
        #             "friendly_name": "",                              #Human readable name assigned to the Device or Node.
        #             "is_online": true,                                #Denotes if node or device is online
        #             "location": "",                                   #Device location name assigned to the Device or Node.
        #             "sounding_warmup": null,                          
        #             "sounding_status": false,                         #Shows sounding status of the device
        #             "sounding_status_score": -1,                      #Shows the status score (-1 means device is not sounding)
        #             "sounding_status_reason": "N/A",                  #reason for device not sounding
        #             "sensitivity_mode": "global",                     #Controls if the device can be used for sounding.
        #             "sensitivity": 1,                                 #Current sensitivity of the device. Only valid when sensitivity_mode = override, otherwise an error will be returned.
        #             "links": [],                                      #Shows links that the device is forming with other device
        #             "id": 133,                                        
        #             "is_root": true,                                  #Shows if device is a master node
        #             "device_id": "csi-b-44d4541e94b0",                #Shows device id created by concating the mac id
        #             "omot_version": null,                             #shows the omot version used in the network
        #             "sounding_mesh": "allow"                          #Shows if sounding is allowed in mesh mode in network
        #         },
        #         {
        #             "mac": "f0:ef:86:06:2b:8d",
        #             "is_node": false,
        #             "is_extender": false,
        #             "friendly_name": "",
        #             "is_online": true,
        #             "location": "",
        #             "sounding_mode": "allow",
        #             "sounding_warmup": null,
        #             "sounding_status": true,
        #             "sounding_status_score": 0.1,
        #             "sounding_status_reason": "N/A",
        #             "sensitivity_mode": "global",
        #             "sensitivity": 1,
        #             "links": [
        #                 {
        #                     "src_id": 133,
        #                     "rssi": "-45",
        #                     "if_ch": 1
        #                 }
        #             ]
        #         }
        #     ]
        # }
        response = requests.get(
            URL + "/sounding/clients/",
            headers = header)                                       
        data = response.json()
        print("GET CLIENTS STATE")
        pprint.pprint(data)

############################################# SOUNDING V2 API ##########################################################

        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        #Incase you have python<3.7 comment both the lines above and replace loop used below with asyncio.run


        #WEBSOCKET API = Live Motion Websocket
        ws_url = "wss://"+ CLOUD_SPACE + "/motions?token=" + token_str + "&network_id=" + id
        ws = websocket(ws_url, 5) 
        t1 = threading.Thread(target=loop, args=(ws.run(),),)
        t1.start()
        t1.join()



     
    

    except Exception as e:
        print (str(e))   


if __name__ == "__main__":
    main()