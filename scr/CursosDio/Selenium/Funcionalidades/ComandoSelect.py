import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
#A cada comando deve esperar no máximo 12 segundos para continuar as tarefas
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')
#Seleciona usando o texto vizualizado 
dropdown_products = Select(browser.find_element(By.XPATH,"//select[@id='first']"))
dropdown_products.select_by_visible_text("Google")
time.sleep(3)
#seleciona usando o valor e muda usando o index
dropdown_animals = Select(browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(3)
dropdown_animals.select_by_index(3)
time.sleep(3)
#Seleciona mais de um
dropdown_food = Select(browser.find_element(By.XPATH,"//select[@id='second']"))
dropdown_food.select_by_visible_text("Pizza")
time.sleep(3)
dropdown_food.select_by_visible_text("Bonda")
time.sleep(2)

