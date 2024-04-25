import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
#A cada comando deve esperar no máximo 12 segundos para continuar as tarefas
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://chercher.tech/practice/implicit-wait-example')

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed(), 'Não está mostrando na tela'
time.sleep(3)
print('Checkbox criado na tela')

browser.quit()

