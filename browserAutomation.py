from selenium import webdriver

waitInterval = 30

browser = webdriver.Chrome('C:\\hehe\\chromedriver.exe')
browser.get('https://fss.virtusa.com/dashboard/')

username = browser.find_element_by_id('userName')
username.send_keys('support')

password = browser.find_element_by_id('userPassword')
password.send_keys('Kan3lbull3')

loginButton = browser.find_element_by_id('loginbuttonID')
loginButton.click()


browser.wait = WebDriverWait(driver,waitInterval)
