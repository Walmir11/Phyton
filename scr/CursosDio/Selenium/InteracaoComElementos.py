import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://saucedemo.com')

userName = browser.find_element(By.ID,'user-name')
password = browser.find_element(By.ID,'password')
btn_login = browser.find_element(By.ID,'login-button')

#send_keys()
userName.send_keys('standard_user')
password.send_keys('secret_sauce')

#Click()
btn_login.click()

#text
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(products_title.text)
assert products_title.text == "Products"

#get_attribute
img_backpack = browser.find_element(By.XPATH, "(//img[@class = 'inventory_item_img'])[1]")
print(img_backpack.get_attribute('alt'))
assert img_backpack.get_attribute('alt'), 'Algo deu errado'