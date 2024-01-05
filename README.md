Instructions to run the api script:

1. Edit homeaware.py file and enter the email and password of the system you are using. Update the CLOUD_SPACE url with the one where your system belongs.
2. Open command prompt (cmd)
3. In cmd window, get to the folder location using "cd C:\Users\xyz\Downloads\api_sequence"
4. Make sure your system has python and pip installed and setup
5. Run "pip install -r requirements.txt"
6. Run "python homeaware.py" or "python3 homeaware.py"
7. To call other apis uncomment or comment lines with print statement as required in the code "motion.py"


Documentation URL: https://api-docs.qatools.csc.wifimotion.ca/view/app-cloud/latest.html

List of APIs used in Caregiver Aware MVP: 

[Logging In]
1. POST Login and Begin Session

[Family Aware BETA]
1. GET Sleep-Wake Settings
2. POST Sleep-Wake Settings
3. GET Household Sleep-Wake Times Data
4. GET Household Activity
5. GET Live Motion Websocket
6. POST Store Device Push Token (To enable notifications)

[Universal Alerting]
1. GET Get alerts from network
2. POST Create a single custom alert.
3. GET Get Universal Alert Status
4. GET Get universal alert
5. DEL Delete Universal Alert
6. PATCH Update of Single Alert
7. PATCH Universal Alert Bulk Enable
