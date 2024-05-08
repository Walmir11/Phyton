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
nomes_streamers = []

# Faça login (substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais)
driver.find_element(By.XPATH,"//button[@data-a-target='login-button']").click()
time.sleep(3)
driver.find_element(By.ID,'login-username').send_keys('giniceu')
driver.find_element(By.ID,'password-input').send_keys('monteirobem10homer')
driver.find_element(By.XPATH,"//button[@data-a-target='passport-login-button']").click()
time.sleep(8)

categorias = ['Just Chatting', 'League of Legends', 'Counter-Strike', 'VALORANT', 'Grand Theft Auto V']

for categoria in categorias:
    driver.get(f'https://www.twitch.tv/directory/game/{categoria}')
    
    dropdown = Select(driver.find_element(By.XPATH,"//*[@class='Layout-sc-1xcs6mc-0 xxjeD' and text()='Mais espectadores']"))
    dropdown.select_by_visible_text('Mais espectadores')
    
    # Raspe as informações dos streamers (você precisará ajustar isso conforme necessário)
    streamers = driver.find_elements(By.XPATH,"//*[@class='tw-image']")
    for streamer in streamers:
        nome_streamer = streamer.text
        nomes_streamers.append({"Nome: ",nome_streamer})

    vizualizacao = driver.find_elements(By.XPATH,"//*[@class='ScMediaCardStatWrapper-sc-anph5i-0 jRUNHm tw-media-card-stat']")

    for visualizacoes in vizualizacao:
        vizualizacao_streamer = visualizacoes.text()
        nomes_streamers.append({"Vizualizações: ",vizualizacao})    

# Crie um DataFrame com os dados
df = pd.DataFrame(nomes_streamers)

# Exiba os 10 streamers com mais visualizações
top_10_streamers = df.nlargest(10, 'Visualizações')
print(top_10_streamers)

# Feche o navegador
driver.quit()
