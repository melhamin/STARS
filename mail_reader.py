import time
import re
import smtplib
import time
import imaplib
import email
import browser as br

from credentials import *

SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 993
MAILBOX = 'inbox'
SEARCH_CRITERIA = 'REVERSE DATE'  # Descending(most recent first)


def Setup():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(EMAIL, APP_PWD)
    mail.select(mailbox=MAILBOX, readonly=True)

    return mail


def GetLatestEmails(mail):
    type, data = mail.search(None, '(SUBJECT "Secure Login Gateway E-Mail Verification Code")')
    mail_ids = data[0]
    id_list = mail_ids.split()

    end = len(id_list)
    start = (end - 3) if end > 3 else end

    return [id_list[i] for i in range(start, end)]

def GetCode(content):
    te = re.search(r'Verification Code: \w+', content)
    ref = te.group(0)
    ind = ref.rfind(' ')
    print(f'ref {ref}')
    return ref[ind+1:]



def ExtractVerificationCode(mail, ids, ref_code):
    for num in ids:
        type, data = mail.fetch(num, '(RFC822)')
        content = str(data[0][1])        
        contains = ref_code in content
        print(content)
        if contains:
            verification_code = GetCode(content)             
            return verification_code


def ReadMail(ref_code):
    try:
        time.sleep(1)
        mail = Setup()        
        ids = GetLatestEmails(mail)     

        verification_code = ExtractVerificationCode(mail, ids, ref_code)                                            
        mail.close()

        return verification_code
    except Exception as e:
        print(f'ERROR[*] {e}')

