import time
import re
import time
import imaplib

from credentials import *

SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 993
MAILBOX = 'inbox'
SEARCH_CRITERIA = 'REVERSE DATE'  # Descending(most recent first)


def Setup():
    """ Connect to the mail server
    """
    print('[+] CONNECTING TO THE MAILBOX...')
    mailbox = imaplib.IMAP4_SSL(SMTP_SERVER)
    mailbox.login(EMAIL, APP_PWD)
    mailbox.select(mailbox=MAILBOX, readonly=True)    
    print('[+] CONNECTED TO MAILBOX')
    return mailbox


def GetLatestEmails(mailbox):
    """ Get latest 3 unseen emails with subject as "Secure Login Gateway E-Mail Verification Code"

        returns a list of last 3 emails
    """        
    type, data = mailbox.search(None, '(SUBJECT "Secure Login Gateway E-Mail Verification Code")')
    mail_ids = data[0]
    id_list = mail_ids.split()
    end = len(id_list)
    start = (end - 3) if end > 3 else end
    return [id_list[i] for i in range(start, end)]

def GetCode(content):
    """ Extract verification code from email body
        
        returns verification code
    """
    te = re.search(r'Verification Code: \w+', content)
    ref = te.group(0)
    ind = ref.rfind(' ')    
    return ref[ind+1:]

def ExtractVerificationCode(mailbox, ids, ref_code):
    """ Searches for reference code in latest 3 emails and extracts verfication code

        returns verfication code
    """
    for num in ids:
        type, data = mailbox.fetch(num, '(RFC822)')
        content = str(data[0][1])        
        contains = ref_code in content        
        if contains:
            verification_code = GetCode(content)                                     
            return verification_code


def ReadMail(ref_code):
    """ Reads mailbox for verfication code

        returns verification code
    """
    try:        
        time.sleep(1)
        mailbox = Setup()        
        print(f'[+] GETTING EMAIL WITH REFERENCE CODE: {ref_code}')
        ids = GetLatestEmails(mailbox)     
        verification_code = ExtractVerificationCode(mailbox, ids, ref_code)   
        print(f'[+] VEERIFICATION CODE IS: {verification_code}')                                         
        mailbox.close()

        return verification_code
    except Exception as e:
        print(f'ERROR[*] {e}')

