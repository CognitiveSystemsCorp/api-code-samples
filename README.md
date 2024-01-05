# Instructions to run the api script:

1. Edit homeaware.py file and enter the email and password of the system you are using. Update the CLOUD_SPACE url with the one where your system belongs.
2. Open command prompt (cmd in Windows) or Terminal in Ubuntu
3. In cmd window, get to the folder location using "cd C:\Users\xyz\Downloads\api-code-samples"
4. Make sure your system has python and pip installed and setup
5. Run "pip install -r requirements.txt"
6. Run "python homeaware.py" or "python3 homeaware.py"
7. To call other apis uncomment or comment lines with print statement as required in the code "motion.py"

Documentation URL: https://api-docs.qatools.csc.wifimotion.ca/view/app-cloud/latest.html

# List of APIs used in Caregiver Aware MVP: 

From the documentation URL given above you will be able to find the apis given below:

[Logging In]
1. POST Login and Begin Session

[Family Aware BETA] - To get / update sleep and activity data
1. GET Sleep-Wake Settings
2. POST Sleep-Wake Settings
3. GET Household Sleep-Wake Times Data
4. GET Household Activity
5. GET Live Motion Websocket

[Firebase Notifications] - To enable fcm notifications, send your device token to app cloud
1. POST Store Device Push Token 

[Universal Alerting] - To get / update Caregiver Aware Alerts
1. GET Get alerts from network
2. POST Create a single custom alert.
3. GET Get Universal Alert Status
4. GET Get universal alert
5. DEL Delete Universal Alert
6. PATCH Update of Single Alert
7. PATCH Universal Alert Bulk Enable

Note: Caregiver aware MVP is not limited to the APIs provided above. It also uses general apis from other sections in documentation

[Network Settings] - To get / update timezone
1. GET Show General Settings (With ID)
2. PUT Update General Settings

[Sounding v2] - To get / update motion sensitivity
1. GET Get Global Settings 
2. PATCH Update Global Settings