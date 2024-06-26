import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(3)
#login
driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
#adicionando ao carrinho
driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()

driver.find_element(By.ID,'back-to-products').click()

driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()

driver.find_element(By.XPATH,"//*[@class='shopping_cart_link']").click()
driver.find_element(By.ID,'checkout').click()

driver.find_element(By.ID,'first-name').send_keys('Walmir')
driver.find_element(By.ID,'last-name').send_keys('Neto')
driver.find_element(By.ID,'postal-code').send_keys('49400000')
time.sleep(3)
driver.find_element(By.XPATH,"//*[@type='submit']").click()
driver.find_element(By.ID,'finish').click()
time.sleep(3)
driver.quit()
