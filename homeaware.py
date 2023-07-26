import requests, threading, asyncio
from lib.websocket_utils import websocket

CLOUD_SPACE = "dummy.cloud.url/api" ## Replace this value with the correct cloud space value for accessing your system 

def main():
    email = "dummy@gmail.com"
    password = "Dummy12345!@#"
    URL = "https://" + CLOUD_SPACE

    try:
        #POST API = Login and Begin Session
        #RESPONSE:  
        # /"refresh_token"
        # /"token"                           ##system generates new token on every call of this api
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
        #print("Token",token_str)

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
        #             "pet_size"             ## Denotes if the user has pet, amd if yes then of what size // Values: none, small, medium, large
        #             "building_type"
        #             "building_size"
        #             "live_enabled"
        #             "subscription_id"
        #             "scene_id"               ## Represents network home/away mode: 4 = home mode, 1 = Away mode
        #             "network_scene_config"   ## To be used later as network scene config id to show and update scene settings
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
        #             "scene_id"              ## To change home/away mode, change the value to: 4 or 1, where 4 = home mode, 1 = Away mode
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



        #GET API = SHOW SCENE SETTINGS
        #RESPONSE:
        # {
        #     "id": xxxx,
        #     "network_id": yyyy,
        #     "excessive_motion_seconds": 600,
        #     "excessive_motion_enabled": true,
        #     "created_at": "2021-10-28T21:36:18.187Z",
        #     "updated_at": "2021-11-26T02:16:26.230Z",
        #     "guardian_enabled": false,
        #     "guardian_weekday_start_time_hours": 6,
        #     "guardian_weekday_start_time_minutes": 0,
        #     "guardian_weekday_end_time_hours": 8,
        #     "guardian_weekday_end_time_minutes": 0,
        #     "auto_switching_enabled": false,                          ## Shows us state for Home/away mode
        #     "guardian_weekend_start_time_hours": 7,
        #     "guardian_weekend_start_time_minutes": 0,
        #     "guardian_weekend_end_time_hours": 9,
        #     "guardian_weekend_end_time_minutes": 0
        # }
        response = requests.get(
            URL + "/network_scene_configs/" + network_scene_config_id,
            headers = header)
        scene_settings_data = response.json()
        #print("guardian_enabled",scene_settings_data["guardian_enabled"])
        #print("auto_switching_enabled",scene_settings_data["auto_switching_enabled"])



        #GET API = UPDATE SCENE SETTINGS
        #RESPONSE:
        # {
        #     "id": xxxx,
        #     "network_id": yyyy,
        #     "excessive_motion_seconds": 600,
        #     "excessive_motion_enabled": true,
        #     "created_at": "2021-10-28T21:36:18.187Z",
        #     "updated_at": "2021-11-26T02:16:26.230Z",
        #     "guardian_enabled": false,
        #     "guardian_weekday_start_time_hours": 6,
        #     "guardian_weekday_start_time_minutes": 0,
        #     "guardian_weekday_end_time_hours": 8,
        #     "guardian_weekday_end_time_minutes": 0,
        #     "auto_switching_enabled": false,                      ## Shows us state for Home/away mode
        #     "guardian_weekend_start_time_hours": 7,
        #     "guardian_weekend_start_time_minutes": 0,
        #     "guardian_weekend_end_time_hours": 9,
        #     "guardian_weekend_end_time_minutes": 0
        # }
        response = requests.put(
            URL + "/network_scene_configs/" + network_scene_config_id,
            data = {
                "id": scene_settings_data["id"],
                "excessive_motion_seconds": scene_settings_data["excessive_motion_seconds"],
                "excessive_motion_enabled": scene_settings_data["excessive_motion_enabled"],
                "guardian_enabled": scene_settings_data["guardian_enabled"],
                "guardian_weekday_start_time_hours": scene_settings_data["guardian_weekday_start_time_hours"],
                "guardian_weekday_start_time_minutes": scene_settings_data["guardian_weekday_start_time_minutes"],
                "guardian_weekday_end_time_hours": scene_settings_data["guardian_weekday_end_time_hours"],
                "guardian_weekday_end_time_minutes": scene_settings_data["guardian_weekday_end_time_minutes"],
                "auto_switching_enabled": scene_settings_data["auto_switching_enabled"],
                "guardian_weekend_start_time_hours": scene_settings_data["guardian_weekend_start_time_hours"],
                "guardian_weekend_start_time_minutes": scene_settings_data["guardian_weekend_start_time_minutes"],
                "guardian_weekend_end_time_hours": scene_settings_data["guardian_weekend_end_time_hours"],
                "guardian_weekend_end_time_minutes": scene_settings_data["guardian_weekend_end_time_minutes"]
            },
            headers = header)                                       ## REQUEST BODY
        data = response.json()
        #print("UPDATE SCENE SETTINGS", data)

        #GET API = Network Topologies
        response = requests.get(
            URL + "/topologies" 
            ,headers = header)
        data = response.json()
        friendly_names = []
        for info in data["devices"]:
            friendly_names.append(info["friendly_name"])              ## Friendly names of all the devices connected in network. Shows serial number if you have not renamed the device
        #print("Network Topologies",str(friendly_names))         



        #GET API = MOTION HISTORY DENSITIES
        #RESPONSE:
        #[
            # [
            #     0.826388888888889,                                  ## Motion Intensity 
            #     1637028000                                          ## TimeStamp when motion of above intensity occured
            # ], ...
        #]
        UTC_TIME_NOW = "1637546100"
        UTC_TIME_01_NOV = "1635731700"

        response = requests.get(
            URL + "/motion_history_densities" 
            #+ "?from="+ UTC_TIME_01_NOV +"&to="+ UTC_TIME_NOW        ## QueryString variables used are optional
            ,headers = header)
        data = response.json()
        #print("Motion History Data",str(data))                        ## Prints an array list of intesities of motion with timestamp when motion occured 
        


############################################# SOUNDING V2 API ##########################################################


    #GET API = GET GLOBAL SETTINGS
        #RESPONSE:
        # {
        #     "motion_events_enabled": 1,      #Enable/Disable the Home/Away mode of network
        #     "motion_events_armed": 1,        #Enable/Disable logging of MotionDetectedEvents in cloud history
        #     "mesh_auto_disable": 0,          #Enable/Disable mesh link sounding on all current and future nodes.     
        #     "sounding_mode": "allow",        #
        #     "leafblower_cutoff": 0,
        #     "zone_priority_list": [
        #         "Router",
        #         "Bhumik room",
        #         "Aidan room",
        #         "Glass"
        #     ],
        #     "sensitivity": 1,
        #     "pet_mode": 0,
        #     "cooldown": 120
        # }
        response = requests.get(
            URL + "/sounding/settings/",
            headers = header)                                       ## REQUEST BODY
        data = response.json()
        print("GET GLOBAL SETTINGS", data)


    #GET API = GET CLIENT STATE
        #RESPONSE:
        # {
        #     "devices": [
        #         {
        #             "is_node": true,
        #             "is_extender": false,
        #             "friendly_name": "",
        #             "is_online": true,
        #             "location": "",
        #             "sounding_warmup": null,
        #             "sounding_status": false,
        #             "sounding_status_score": -1,
        #             "sounding_status_reason": "N/A",
        #             "sensitivity_mode": "global",
        #             "sensitivity": 1,
        #             "links": [],
        #             "id": 133,
        #             "is_root": true,
        #             "device_id": "csi-b-44d4541e94b0",
        #             "omot_version": null,
        #             "sounding_mesh": "allow"
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
            headers = header)                                       ## REQUEST BODY
        data = response.json()
        print("GET CLIENTS STATE", data)

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
