import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID,'username')
checkbox_remembar_me = browser.find_element(By.XPATH,"//*[@type= 'checkbox']")

# is_displayed()
print(username.is_displayed())
assert username.is_displayed(),'Aconteceu algum erro'