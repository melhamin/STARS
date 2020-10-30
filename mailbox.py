import time
import re
import time
import imaplib

import configurations as configs

MAILBOX_FOLDER = 'inbox'

class MailBox:        

    def __init__(self, server, port) -> None:
        self.server = server
        self.port = port
        self.mailbox = self.setup()

    def setup(self):
        """ Connect to the mail server
        """   
        print('[+] CONNECTING TO THE MAILBOX...')                
        mailbox = imaplib.IMAP4_SSL(self.server, self.port)    
        mailbox.login(configs.EMAIL, configs.APP_PWD)
        mailbox.select(mailbox=MAILBOX_FOLDER, readonly=True)    
        print('[+] CONNECTED TO THE MAILBOX')
        return mailbox


    def get_latest_emails(self):
        """ Get latest 3 unseen emails with subject as "Secure Login Gateway E-Mail Verification Code"
            returns a list of last 3 emails
        """        
        self.mailbox.select()
        type, data = self.mailbox.search(None, '(SUBJECT "Secure Login Gateway E-Mail Verification Code")')
        mail_ids = data[0]
        id_list = mail_ids.split()
        end = len(id_list)
        start = (end - 3) if end > 3 else end
        return [id_list[i] for i in range(start, end)]

    def get_Code(self, content):
        """ Extract verification code from email body        
            return: verification code
        """
        te = re.search(r'Verification Code: \w+', content)
        ref = te.group(0)
        ind = ref.rfind(' ')    
        return ref[ind+1:]

    def extract_verfication_code(self, ids, ref_code):
        """ Searches for reference code in latest 3 emails and extracts verfication code
            return: verfication code
        """
        for num in ids:
            type, data = self.mailbox.fetch(num, '(RFC822)')
            content = str(data[0][1])        
            contains = ref_code in content        
            if contains:
                verification_code = self.get_Code(content)                                     
                return verification_code


    def get_verification_code(self,ref_code):
        """ Reads mailbox for verfication code
            return: verification code
        """
        try:        
            time.sleep(1)               
            print(f'[+] GETTING EMAIL WITH REFERENCE CODE: {ref_code}')
            ids = self.get_latest_emails()     
            verification_code = self.extract_verfication_code(ids, ref_code)   
            print(f'[+] VEERIFICATION CODE IS: {verification_code}')                                         
            self.mailbox.close()            

            return verification_code
        except Exception as e:
            print(f'ERROR[*] {e}')

