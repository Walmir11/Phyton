import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge()
#Tempo máximo esperado para um elemento funcionar
browser.maximize_window()
browser.get('https://chercher.tech/practice/frames')
#Colocando endereço do iframe em uma variavel
iframe1 = browser.find_element(By.ID,'frame1')
#Mudar o foco do browser para o iframe criado
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH,"//*[@id='topic']/following-sibling::input").send_keys('iframe1')
time.sleep(2)
#para acessar um iframe dentro do outro tem que acessar as estremidades primeiro
iframe3 = browser.find_element(By.ID, 'frame3')
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.ID, 'a')
checkbox.click()
time.sleep(2)
#Voltando pra raiz da página para entrar em outro iframe
browser.switch_to.default_content()
iframe2 = browser.find_element(By.ID,'frame2')
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(2)
