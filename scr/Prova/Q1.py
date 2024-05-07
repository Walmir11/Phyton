# Importe as bibliotecas necessárias
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Acesse a página do Twitch
driver.maximize_window()
driver.get('https://www.twitch.tv/')

# Faça login (substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais)
driver.find_element(By.XPATH,"//button[@data-a-target='login-button']").click()
time.sleep(3)
driver.find_element(By.ID,'login-username').send_keys('giniceu')
driver.find_element(By.ID,'password-input').send_keys('monteirobem10homer')
driver.find_element(By.XPATH,"//button[@data-a-target='passport-login-button']").click()
time.sleep(8)

# Navegue até as categorias desejadas (por exemplo, Just Chatting)
driver.get('https://www.twitch.tv/directory/game/Just%20Chatting')

dropdown = Select(driver.find_element(By.XPATH,"//*[@class='Layout-sc-1xcs6mc-0 xxjeD' and text()='Mais espectadores']"))
dropdown.select_by_visible_text('Mais espectadores')

# Raspe as informações dos streamers (você precisará ajustar isso conforme necessário)
streamers = driver.find_elements(By.XPATH,"//*[@class='tw-image']")
streamer_data = []
for streamer in streamers:
    name = streamer.find_element('.tw-font-size-5.tw-semibold.tw-mg-t-05').text
    views = streamer.find_element('.tw-font-size-6.tw-semibold.tw-mg-t-05').text
    streamer_data.append({'Nome': name, 'Visualizações': views})

# Crie um DataFrame com os dados
df = pd.DataFrame(streamer_data)

# Exiba os 10 streamers com mais visualizações
top_10_streamers = df.nlargest(10, 'Visualizações')
print(top_10_streamers)

# Feche o navegador
driver.quit()
