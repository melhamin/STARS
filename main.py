from browser_launcher import LaunchBrowser
import browsers as br

# Supported Providers
GOOGLE_SMTP_SERVER = 'imap.gmail.com'  
GOOGLE_SMTP_PORT = 993
OUTLOOK_SMTP_SERVER = 'outlook.office365.com'
OUTLOOK_SMTP_PORT = 993
YAHOO_SMTP_SERVER = 'smtp.mail.yahoo.com'
YAHOO_SMTP_PORT = 465


if __name__ == "__main__":
    print('[+] LAUNCHING STARS...')        
    drivder = LaunchBrowser(browser=br.FIREFOX, server=GOOGLE_SMTP_SERVER, port=GOOGLE_SMTP_PORT)