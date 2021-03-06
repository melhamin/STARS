import re
import time

import browsers as br
import configurations as configs

URL = 'https://stars.bilkent.edu.tr'

class Browser:        
    def __init__(self, browser_name) -> None:
        self.browser_name = browser_name
        self.driver = self.setup_driver()

    def setup_driver(self):
        ''' Initialize the browser
            browser: is the name of the browser which is going to be used
        '''
        return br.get_browser(self.browser_name)
    
    def nav_to_srs(self):
        """ Navigate to SRS login page            
        """
        try:
            print(f'[+] OPENNING {URL}...')
            self.driver.get(URL)
        except Exception as e:
            print('[*] ERROR: SOMETHING WENT WRONG! RETRYING...')
            self.driver.get(URL)

        print('[+] OPENNING SRS LOGIN PAGE...')
        # The xPath for SRS 
        self.driver.find_element_by_xpath('//*[@id="services"]/li[3]/a').click()        

    def get_password_field_id(self):
        """Extracts unique part of xPath for password field. It is needed because 
            xPath for password field is unique in every request
            return: Password field xPath id if found, None otherwise
        """        
        page_source = self.driver.page_source
        matches = re.findall(r'LoginForm-\w+', page_source)
        return None if len(matches) == 0 else matches[0]    
        
    def extract_reference_code(self, text):
        """ Extracts verification code reference code for 2-Step verificaiton from email body
            return: reference code
        """
        print('[+] GETTING REFERENCE CODE...')
        te = re.search(r'reference code \w+', text)
        ref = te.group(0)
        ind = ref.rfind(' ')
        ref_code = ref[ind+1:]
        print(f'[+] REFERENCE CODE IS: {ref_code}')
        return ref_code


    def login(self):
        """ Login user with ID and password
            return: verification reference code
        """
        ID_xPath = '//*[@id="LoginForm_username"]'
        PWD_xPath = f'//*[@id="{self.get_password_field_id()}"]'
        SUBMIT_xPath = '//*[@id="login-form"]/fieldset/div/div[1]/div[3]/button'

        VER_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[1]/div/p[2]'

        # pass keys
        print('[+] ENTERING ID AND PASSWORD...')
        self.driver.find_element_by_xpath(ID_xPath).send_keys(configs.BILKENT_ID)
        self.driver.find_element_by_xpath(PWD_xPath).send_keys(configs.PASSWORD)
        self.driver.find_element_by_xpath(SUBMIT_xPath).click()

        time.sleep(1)
        # get verification code reference    
        VERIFICATION_CODE_REF = self.driver.find_element_by_xpath(VER_xPath)
        ref = VERIFICATION_CODE_REF.text

        return self.extract_reference_code(ref)


    def verify(self, verification_code):
        """ Verify user by using verfication_code        
        """
        VERF_xPath = '//*[@id="EmailVerifyForm_verifyCode"]'
        BTN_xPath = '//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[2]/button'
        self.driver.find_element_by_xpath(VERF_xPath).send_keys(verification_code)
        self.driver.find_element_by_xpath(BTN_xPath).click()            

    def launch_browser(self):
        """ Launch browser and log in
            return: 2-step verification referenece code
        """
        print('[+] OPENNING BROWSER...')
        # driver = self.InitializeBrowser(browser=browser)
        try:
            self.nav_to_srs()                                       
            try:                                               
                ref_code = self.login()
            except Exception as e:
                print('[*] ERROR: Oops! FAILED TO LOGN, RETRYING...')
                self.driver.refresh()                
                ref_code = self.login()                       

            return ref_code
            
        except KeyboardInterrupt:
            self.driver.quit()
            self.driver.close()
            print('[*] Exitting....')
