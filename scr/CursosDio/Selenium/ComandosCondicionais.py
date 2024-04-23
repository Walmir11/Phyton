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

# is_enabled
print(username.is_enabled())
assert username.is_enabled(),'Aconteceu algum erro'

#is_select
print(checkbox_remembar_me.is_selected())
assert not checkbox_remembar_me.is_selected(), 'Aconteceu algum erro'

#Clicando no checkbox
time.sleep(2)
checkbox_remembar_me.click()
time.sleep(2)


print(checkbox_remembar_me.is_selected())
assert checkbox_remembar_me.is_selected(), 'Aconteceu algum erro'
