from selenium import webdriver
import selenium.webdriver.chrome.options as ChromeOptions
import selenium.webdriver.firefox.options as FirefoxOptions

CHROME = 'chrome'
FIREFOX = 'firefox'

def Chrome():
    options = ChromeOptions.Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options) 
    return driver

def Firefox():
    options = FirefoxOptions.Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(options=options)
    return driver