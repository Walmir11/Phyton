import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.climatempo.com.br')
driver.implicitly_wait(3)
time.sleep(3)

driver.find_element(By.ID,'Botao_mais_detalhes_card_tempo_no_momento').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@itemprop="name" and text()="Cidade"]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]').click()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='Botao_barra_navegacao_15_dias'][@class='link actTriggerGA']").click()
time.sleep(2)


    