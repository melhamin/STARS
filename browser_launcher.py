import re
import requests
import time

import browsers as br
import mail_reader as mailbox
from credentials import *

URL = 'https://stars.bilkent.edu.tr'

def GetPasswordFieldID(url):
    """Extracts unique part of xPath for password field. It is needed because 
        xPath for password field is unique for every request

        id = Password field xPath id
    """
    res = requests.get(url)
    val = re.search(r'LoginForm-\w+', str(res.content)).group(0)
    split_index = val.find('-')
    id = val[split_index + 1:]
    return id
    


def ExtractVerificationCodeRef(text):
    """ Extracts verification code reference code for 2-Step verificaiton from email body

        ref_code = Reference code 
    """

    print('[+] GETTING REFERENCE CODE...')
    te = re.search(r'reference code \w+', text)
    ref = te.group(0)
    ind = ref.rfind(' ')
    ref_code = ref[ind+1:]
    print(f'[+] REFERENCE CODE IS: {ref_code}')
    return ref_code


def Login(driver, pwd_field_id):
    """ Login user with ID and password

        returns verification reference code
    """
    ID_xPath = '//*[@id="LoginForm_username"]'
    PWD_xPath = f'//*[@id="LoginForm-{pwd_field_id}"]'
    SUBMIT_xPath = '//*[@id="login-form"]/fieldset/div/div[1]/div[3]/button'

    VER_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[1]/div/p[2]'

    # pass keys
    print('[+] ENTERING ID AND PASSWORD...')
    driver.find_element_by_xpath(ID_xPath).send_keys(BILKENT_ID)
    driver.find_element_by_xpath(PWD_xPath).send_keys(PASSWORD)
    driver.find_element_by_xpath(SUBMIT_xPath).click()

    time.sleep(1)
    # get verification code reference    
    VERIFICATION_CODE_REF = driver.find_element_by_xpath(VER_xPath)
    ref = VERIFICATION_CODE_REF.text

    return ExtractVerificationCodeRef(ref)


def Verify(driver, verification_code):
    """ Verify user by using verfication_code        
    """
    VERF_xPath = '//*[@id="EmailVerifyForm_verifyCode"]'
    BTN_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[2]/button'
    driver.find_element_by_xpath(VERF_xPath).send_keys(verification_code)
    driver.find_element_by_xpath(BTN_xPath).click()    

def NavToSRS(driver):
    """ Navigate to SRS login page

        returns current page url
    """
    try:
        print(f'[+] OPENNING {URL}...')
        driver.get(URL)
    except Exception as e:
        print('[*] SOMETHING WENT WRONG! RETRYING...')
        driver.get(URL)

    print('[+] OPENNING SRS LOGIN PAGE...')
    driver.find_element_by_xpath('//*[@id="services"]/li[3]/a').click()
    return driver.current_url

def InitializeBrowser(browser):
    if browser == br.FIREFOX:
        return br.Firefox()
    elif browser == br.CHROME:
        return br.Chrome()        

def LaunchBrowser(browser, server, port):
    """ Launch browser and log in
    """
    print('[+] OPENNING BROWSER...')
    driver = InitializeBrowser(browser=browser)
    try:
        current_url = NavToSRS(driver)
        pwd_field_id = GetPasswordFieldID(current_url)        
        try:                                               
            ref_code = Login(driver, pwd_field_id)
        except Exception as e:
            print('[*] Oops! COULD NOT LOGN, RETRYING...')
            driver.refresh()
            pwd_field_id = GetPasswordFieldID(current_url)
            ref_code = Login(driver, pwd_field_id)
        
        # Get verification code
        verification_code = mailbox.ReadMail(ref_code, server, port)
        retry = verification_code is None        
        while retry:
            print('[*] Oops! SOMETHING WENT WRONG, RETRYING...')
            verification_code = mailbox.ReadMail(ref_code, server, port)
            retry = verification_code is None
        
        print(f'[+] VERIFYING...')
        Verify(driver, verification_code)
        print('[+++] SUCCESSFULLY LOGGED IN')

        return driver
        
    except KeyboardInterrupt:
        print('[*] Exitting....')
