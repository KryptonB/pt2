import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# Sleep times to pause the script (given in seconds)
shortInterval = 2
longInterval = 25

# Selenium Chrome driver location
chromeDriverPath = 'C:\\Python27\\Custom_tools\\chromedriver.exe'

# Login credentials for support user
dashboardUsername = 'support'
dashboardPassword = 'Kan3lbull3'

# IDs for clickable elements
usernameTextboxID = 'userName'
passwordTextboxID = 'userPassword'
hideAllButtonID = 'selectAllNoneDisplayOption'
stopNotificationsButtonID = 'selectNotificationAllNoneOption'
disableSoundsButtonID = 'selectSoundAllNoneOption'

# Active Client lists
displayClientList = ['HUSQVARNAShowHideCheckBox', 'ELECTROLUXShowHideCheckBox', 'ERICSSONShowHideCheckBox', 'SASShowHideCheckBox', 'FMOShowHideCheckBox', 'LANDSHYPOTEKShowHideCheckBox', 'SBABShowHideCheckBox', 'SEBShowHideCheckBox', 'SPFShowHideCheckBox', 'TTCShowHideCheckBox', 'VOLVO_LVShowHideCheckBox']
popupClientList = ['HUSQVARNANotificationCheckBox', 'ELECTROLUXNotificationCheckBox', 'ERICSSONNotificationCheckBox', 'SASNotificationCheckBox', 'FMONotificationCheckBox', 'LANDSHYPOTEKNotificationCheckBox', 'SBABNotificationCheckBox', 'SEBNotificationCheckBox', 'SPFNotificationCheckBox', 'TTCNotificationCheckBox', 'VOLVO_LVNotificationCheckBox']



def initiateBrowserWindow():
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=C:\\mybrowser\\')
    browser = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=options)
    browser.get('https://fss.virtusa.com/dashboard/')
    return browser

    

def loginToDashboard(usernameTextboxID, passwordTextboxID):
    username = browser.find_element_by_id(usernameTextboxID)
    username.click()
    username.clear()
    username.send_keys(dashboardUsername)

    password = browser.find_element_by_id(passwordTextboxID)
    password.click()
    password.clear()
    password.send_keys(dashboardPassword)

    loginButton = browser.find_element_by_id('loginbuttonID')
    loginButton.click()

    
# Function to hide inactive clients from the main dashboard tab  
def hideClients(displayClientList):
    for client in displayClientList:
        xClient = browser.find_element_by_id(client)
        xClient.click()

      

# Function to stop notifications from inactive clients
def stopNotifications(popupClientList):
    for client in popupClientList:
        xClient = browser.find_element_by_id(client)
        xClient.click()


      
# Function to move to "Settings" tab
def moveToSettingsTab():
    settingsTab = browser.find_element_by_link_text('Settings')
    settingsTab.click()
    
    

# Function to move to "Dashboard" tab
def moveToDashboardTab():
    dashboardTab = browser.find_element_by_xpath('//*[@id="form1"]/div[3]/div[5]/div/ul/li[1]/a')
    dashboardTab.click()

   

# Function to click the "Show/Hide Notifications" button
def stopNotificationsButtonClick(stopNotificationsButtonID):
    notificationButton = browser.find_element_by_id(stopNotificationsButtonID)
    notificationButton.click()

   
# Function to click the "Show/Hide All Clients" button
def hideAllClients(hideAllButtonID):
    hideAllButton = browser.find_element_by_id(hideAllButtonID)
    hideAllButton.click()

    
# Function to click the "Stop Sounds" button
def disableSounds(disableSoundsButtonID):
    disableSoundsButton = browser.find_element_by_id(disableSoundsButtonID)
    disableSoundsButton.click()


# Initialize the browser 
browser = initiateBrowserWindow()

loginToDashboard(usernameTextboxID, passwordTextboxID)
time.sleep(longInterval)

moveToSettingsTab()
time.sleep(shortInterval)

hideAllClients(hideAllButtonID)
hideClients(displayClientList)
time.sleep(shortInterval)

stopNotificationsButtonClick(stopNotificationsButtonID)
stopNotifications(popupClientList)
time.sleep(shortInterval)

disableSounds(disableSoundsButtonID)
time.sleep(shortInterval)

moveToDashboardTab()
