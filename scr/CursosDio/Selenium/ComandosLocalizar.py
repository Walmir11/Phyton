import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://saucedemo.com')

#find_element(Localiza o elementos)
#userName = browser.find_element(By.ID,'user-name')
#password = browser.find_element(By.ID,'password')

#find_elements(Localiza mais de um elemento)
auth_fields = browser.find_elements(By.XPATH,"//*[@class='input_error form_input']")
print(auth_fields)
print(len(auth_fields))
#verificação
assert len(auth_fields)==2,'Tamanho não condiz com o esperado'

#send_keys(Escreve os textos no campos)
#userName.send_keys('standard_user')
#password.send_keys('secret_sauce')

time.sleep(3)


browser.quit()
