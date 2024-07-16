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
# Pesquisa por 'Lagarto'
search_box = driver.find_element(By.ID, "searchGeneral")
search_box.send_keys('Lagarto')
time.sleep(3)
try:
    # Aguarda a lista de autocomplete aparecer
    wait = WebDriverWait(driver, 10)
    autocomplete_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='searchGeneral_autocomplete']/li[1]")))

    # Usa ActionChains para clicar no item da lista de autocomplete
    driver.find_element(By.XPATH, "//*[@id='searchGeneral_autocomplete']/li[1]").click
    time.sleep(3)
except Exception as e:
    print(f"Erro ao selecionar o item da lista de autocomplete: {e}")
finally:
    time.sleep(3)
    driver.quit()
