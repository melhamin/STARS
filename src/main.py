import sys

from browser_driver import Browser
from mailbox import MailBox
import configurations as configs
import services as services

if __name__ == "__main__":    
    browser = configs.BROWSER
    mail_provider = configs.EMAIL_PROVIDER

    if browser not in services.supported_browsers:
        print('[*] ERROR: INVALID BROWSER CONFIGURATIONS. CHECK YOUR SETTINGS.')
        sys.exit()         

    if mail_provider not in services.supported_providers:
        print('[*] ERROR: INVALID EMAIL PROVIDER CONFIGURATIONS. CHECK YOUR SETTINGS.')
        sys.exit()     

    # Get email provider server and port details
    email_details = services.supported_providers[mail_provider]    
    print('[+] LAUNCHING STARS...')            
    webdriver = Browser(browser)    
    ref_code = webdriver.launch_browser()

    if(ref_code != None):
        # # Get verification code
        mailbox = MailBox(email_details[0], email_details[1])
        verification_code = mailbox.get_verification_code(ref_code)

        retry = verification_code is None                
        while retry:
            print('[*] Oops! SOMETHING WENT WRONG, RETRYING...')
            verification_code = mailbox.get_verification_code(ref_code)
            retry = verification_code is None
        
        print(f'[+] VERIFYING...')
        webdriver.verify(verification_code)
        print('[+++] SUCCESSFULLY LOGGED IN')          

