import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge()
#Tempo máximo esperado para um elemento funcionar
browser.maximize_window()
browser.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
wait = WebDriverWait(browser,30)

# Alert is present
browser.find_element(By.ID, 'alert').click()
#Espera até as condições esperadas acontecerem
wait.until(EC.alert_is_present())
time.sleep(3)

# text_to_be_present_in_element
browser.find_element(By.ID, 'populate-text').click()
#Espera até o texto apareça, tem que passar o locator e o texto esperado
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h2[@class='target-text']"),'Selenium Webdriver'))
target_text = browser.find_element(By.XPATH, "//h2[@class='target-text']").text
assert target_text == 'Selenium Webdriver'

#Deixar elemento clicável
browser.find_element(By.ID,'display-other-button').click()
wait.until(EC.element_to_be_clickable((By.ID,'hidden')))

browser.find_element(By.ID,'checkbox').click()
checkbox = browser.find_element(By.ID,"ch")
wait.until(EC.element_to_be_selected(checkbox))
time.sleep(2)