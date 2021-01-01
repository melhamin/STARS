from selenium import webdriver
import selenium.webdriver.chrome.options as ChromeOptions
import selenium.webdriver.firefox.options as FirefoxOptions
import selenium.webdriver.edge.options as EdgeOptions

def chrome():
    options = ChromeOptions.Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options) 
    return driver

def firefox():
    options = FirefoxOptions.Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(options=options)
    return driver

def safari():
    driver = webdriver.Safari()
    return driver

def edge():        
    driver = webdriver.Edge()
    return driver

def get_browser(name):
    if name == 'chrome':
        return chrome()
    elif name == 'firefox':
        return firefox()
    elif name == 'safari':
        return safari()
    elif name == 'edge':
        return edge()