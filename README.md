# STARS

A python script for automating Bilkent University SRS - Student Academic Information Registration System - login process (with 2-Step verification set to email).

## Usage

1. Install the packages needed:
    ```sh
    pip install selenium requests
    ```
    *install [pip](https://pypi.org/project/pip/) if not already installed

2. Install webdriver:
    - Follow this guide to setup the webdriver according to your browser [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

3. Setup your app password according to your email provider:                
    - For gamil use [this guide](https://support.google.com/mail/answer/185833?hl=en-GB)
    - For yahoo use [this guide](https://help.yahoo.com/kb/generate-third-party-passwords-sln15241.html)
    - For outlook use [this guide](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)        
        
    
3. Configure settings in [main.py](https://github.com/melhamin/STARS/blob/master/main.py):
    - Set browser to be used according to the webdriver you installed
    - Set smtp server and port according to your email provider

4. Add your credentials as stated in [credentials.py](https://github.com/melhamin/STARS/blob/master/credentials.py)

5. Run and enjoy:
    ```sh
    python main.py
    ```
    
## Create an executable and open STARS by one click
<details><summary><b>Show instructions</b></summary>
  
1. Install pyinstaller:
    ```sh
    pip install pyinstaller
    ```
2. Run the following command:
    ```sh
    python pyinstaller --onefile main.py
    ```
3. Run the executable created in /dist directory
  
