# Scientific Collaboration Network
This repository consists of all the scripts that I scripted as a class project named as Scientific Collaboration Network during Networks of Life course (7th semester B.Tech). 

# Steps to send multiple emails using python and gmail.
These steps requires verification of sender's email id.

### Step-1: Extract sendEmail folder
Extract attached folder on your Desktop. 

### Step-2: Enable gmail API
Open link below and follow step-1 to step-4. Download credentials.json file and paste it inside sendEmail folder. 
https://developers.google.com/drive/api/v3/quickstart/python

### Step-3: Authentication
if you can see 'The authentication flow has completed.' on the webpage then authentication with your email id was successful else follow above link for troubleshooting. 

### Step-4: client_secret.json
Follow step-1 provided as an answer by apadana on Stack Overflow. Save file as client_secret.json in same directory. 
https://stackoverflow.com/a/37267330

### Step-5: Excecute 
Excecute script using any one of these (depends on python version and path variable)

python sendEmail.py
Or
python3 sendEmail.py
Or
py -3 sendEmail.py

If something like this is displayed then email is sent successfully else explore Stack Overflow for solution. Thanks!
