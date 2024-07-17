import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configurações do driver
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)
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

driver.find_element(By.XPATH, "(//*[@id='Botao_barra_navegacao_15_dias'])[1]").click()
time.sleep(2)
