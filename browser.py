from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import re
import requests
import time

import mail_reader as mail
from credentials import *

URL = 'https://stars.bilkent.edu.tr'


def GetPasswordFieldID(url):
    # get website HTML content to fetch password field xpath
    res = requests.get(url)
    val = re.search(r'LoginForm-\w+', str(res.content)).group(0)
    split_index = val.find('-')
    id = val[split_index + 1:]
    return id


def ExtractVerificationCodeRef(text):
    te = re.search(r'reference code \w+', text)
    ref = te.group(0)
    ind = ref.rfind(' ')
    return ref[ind+1:]

def Login(driver, pwd_field_id):
    # get xpaths for form fields
    ID_xPath = '//*[@id="LoginForm_username"]'
    PWD_xPath = f'//*[@id="LoginForm-{pwd_field_id}"]'
    SUBMIT_xPath = '//*[@id="login-form"]/fieldset/div/div[1]/div[3]/button'

    VER_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[1]/div/p[2]'
    
    # pass keys
    driver.find_element_by_xpath(ID_xPath).send_keys(BILKENT_ID)
    driver.find_element_by_xpath(PWD_xPath).send_keys(PASSWORD)
    driver.find_element_by_xpath(SUBMIT_xPath).click()

    time.sleep(1)
    # get verification code reference
    VERIFICATION_CODE_REF = driver.find_element_by_xpath(VER_xPath)
    ref = VERIFICATION_CODE_REF.text
    
    return ExtractVerificationCodeRef(ref)

def Verify(driver, verification_code):
    VERF_xPath = '//*[@id="EmailVerifyForm_verifyCode"]'
    BTN_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[2]/button'
    driver.find_element_by_xpath(VERF_xPath).send_keys(verification_code)
    driver.find_element_by_xpath(BTN_xPath).click()    

def NavToSRS(driver):
    driver.get(URL)
    driver.find_element_by_xpath('//*[@id="services"]/li[3]/a').click()  
    return driver.current_url    

ref_code  = None    
def LaunchBrowser():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        current_url = NavToSRS(driver)
        # get password field id
        pwd_field_id = GetPasswordFieldID(current_url)    
                    
        ref_code = Login(driver, pwd_field_id)
        
        verification_code = mail.ReadMail(ref_code)     
        retry = verification_code is None
        while retry:
            print('[*] Oops! Something went wrong. Retrying...')            
            verification_code = mail.ReadMail(ref_code)   
            retry = verification_code is None

        Verify(driver, verification_code)

        while True:
            pass
    except KeyboardInterrupt:
        print('Exitting....')