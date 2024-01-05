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
POST Login and Begin Session

[Family Aware BETA]
GET Sleep-Wake Settings
POST Sleep-Wake Settings
GET Household Sleep-Wake Times Data
GET Household Activity
GET Live Motion Websocket
POST Store Device Push Token (To enable notifications)

[Universal Alerting]
GET Get alerts from network
POST Create a single custom alert.
GET Get Universal Alert Status
GET Get universal alert
DEL Delete Universal Alert
PATCH Update of Single Alert
PATCH Universal Alert Bulk Enable
