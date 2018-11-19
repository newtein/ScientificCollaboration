Sending multiple emails using python and gmail.
Paste the file with emails (details_v3.csv) inside sendEmail directory and follow below steps required for verification of sender's email id.

### Step-1: Extract sendEmail folder
Extract attached folder on your Desktop. 

### Step-2: Enable gmail API
Open link below and follow step-1 to step-4. Download credentials.json file and paste it inside sendEmail folder. 
https://developers.google.com/drive/api/v3/quickstart/python
<img src='screenshots/S1.PNG'/>

### Step-3: Authentication
if you can see 'The authentication flow has completed.' on the webpage then authentication with your email id was successful else follow above link for troubleshooting. 
<img src='screenshots/S2.PNG'/>

### Step-4: client_secret.json
Follow step-1 provided as an answer by apadana on Stack Overflow. <b> Rename file as client_secret.json and paste it in sendEmail directory </b>. 
https://stackoverflow.com/a/37267330
<img src='screenshots/S3.PNG'/>
<img src='screenshots/S4.PNG'/>

### Step-5: Excecute 
Excecute script using any one of these (depends on python version and path variable)

                                                      python sendEmail.py
                                                      Or
                                                      python3 sendEmail.py
                                                      Or
                                                      py -3 sendEmail.py
<img src='screenshots/S5.PNG'/>
If something like this is displayed then email is sent successfully else explore Stack Overflow for solution. 