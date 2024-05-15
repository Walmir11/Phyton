from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('zzzzzzz')
driver.find_element(By.ID,'login-button').click()
assert len(driver.find_element(By.XPATH,'//span[@class="title"]'))==0
time.sleep(2)
