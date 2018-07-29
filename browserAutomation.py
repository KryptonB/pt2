from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

waitInterval = 30

options = webdriver.ChromeOptions()
#options.add_argument('user-data-dir=C:\\Users\\sratnappuli\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\')
options.add_argument('user-data-dir=C:\\mybrowser\\')
browser = webdriver.Chrome(executable_path='C:\\hehe\\chromedriver.exe', chrome_options=options)
browser.get('https://fss.virtusa.com/dashboard/')

username = browser.find_element_by_id('userName')
username.click()
username.clear()
username.send_keys('support')

password = browser.find_element_by_id('userPassword')
password.clear()
password.send_keys('Kan3lbull3')

loginButton = browser.find_element_by_id('loginbuttonID')
loginButton.click()


#browser.wait = WebDriverWait(driver,waitInterval)
