# Automated STARS Login

A Python script for automating Bilkent University SRS - Student Academic Information Registration System - login process (with 2-Step verification set to email).

## Setup and Usage

3. Install Python and pip(if not already):           
    - [Download and install Python](https://www.python.org/downloads/)
    - [Install pip](https://pypi.org/project/pip/)

1. Install the required packages:
    - In command prompt/terminal navigate to the STARS folder and run the following command
    ```sh
    pip install -r requirements.txt
    ```    

2. Install webdriver:
    - Follow [this](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) guide to setup the webdriver according to your browser 

3. Create an app password for your email provider:                
    - For Gamil use [this guide](https://support.google.com/mail/answer/185833?hl=en-GB)
    - For Yahoo use [this guide](https://help.yahoo.com/kb/generate-third-party-passwords-sln15241.html)
    - For Outlook use [this guide](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)    
    ```sh
    If you are using Bilkent webmail or you don't have 2-step authentication turned on for your email, 
    you don't need and app password. Use your email password instead.
    ```    
        
    
3. Add the information required in [configurations.py](https://github.com/melhamin/STARS/blob/master/configurations.py):    
    
    ```sh
    - Type the name of the browser to be used based on the step 2
    - Type the name of your email provider
    ```  

5. Run and enjoy:
    ```sh
    python main.py
    ```
    
## Create an executable and open STARS by one click
  
1. In the command prompt/terminal navigate to the STARS folder and run the following command:
    ```sh
    python pyinstaller --onefile main.py
    ```
2. Run the executable created in /dist directory
  
