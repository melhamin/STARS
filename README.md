# Automated STARS Login

A Python script for automating Bilkent University SRS - Student Academic Information Registration System - login process (with 2-Step verification set to email).

<p float="left">   
  <img src="https://user-images.githubusercontent.com/48331678/98185929-b7ea5600-1f1e-11eb-920f-343eb9f23e68.gif" width="100%" height="50%" alt="flutter chat app instant chat app"/>   

## Setup and Usage

1. Download or clone the project

2. Install Python(if not already):           
    - [Download and install Python](https://www.python.org/downloads/)    

3. Install the webdriver:
    - If you want to use Safari, run the following command in the terminal:
        ```sh
        safaridriver --enable
        ```
    - For other browsers follow [this guide.](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

4. Create your app password:   
    ```sh
    Skip this step if you are using Bilkent webmail or you don't have 2-step verification turned on for your email, 
    you don't need and app password. Use your email password instead.
    ```    
    - For Gamil use [this guide](https://support.google.com/mail/answer/185833?hl=en-GB)
    - For Yahoo use [this guide](https://help.yahoo.com/kb/generate-third-party-passwords-sln15241.html)
    - For Outlook use [this guide](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)    
            
5. Add the information required in [configurations.py](https://github.com/melhamin/STARS/blob/master/configurations.py).    
    
## Create an executable and open STARS by one click
  
### Windows                  
  ```sh
  Open windows-installer.bat 
  ```       
   Stars executable will be created in the "dist" folder.
   
     
### Mac            
   In the terminal navigate to the STARS folder and run the following commands:        
        
  ```sh
   chmod +x mac-installer
   ./mac-installer   
  ```  
     
   Run STARS!

        
     
     
   
    
  
