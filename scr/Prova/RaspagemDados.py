import pandas as pd
from selenium import webdriver
import itertools
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

# Acesse a página do Twitch
driver.maximize_window()
driver.get('https://www.twitch.tv/')
driver.implicitly_wait(12)
info_streamers = []

# Faça login (substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais)
driver.find_element(By.XPATH, "//*[@data-a-target='login-button']").click()
driver.find_element(By.ID,'login-username').send_keys('giniceu')  # Substitua com seu nome de usuário
driver.find_element(By.ID,'password-input').send_keys('monteirobem10')   # Substitua com sua senha
driver.find_element(By.XPATH,"//button[@data-a-target='passport-login-button']").click()

categorias = ['Just Chatting', 'League of Legends', 'Counter-Strike', 'VALORANT', 'Grand Theft Auto V']

for categoria in categorias:
    driver.get(f'https://www.twitch.tv/directory/game/{categoria}')    
    
    # Raspe as informações dos streamers
    streamers = driver.find_elements(By.XPATH,"//*[@class='CoreText-sc-1txzju1-0 gBknDX'] ")
    vizualizacao = driver.find_elements(By.XPATH,"//*[@class='ScMediaCardStatWrapper-sc-anph5i-0 jRUNHm tw-media-card-stat']")
    links = driver.find_elements(By.XPATH,"//*[@data-a-target='preview-card-image-link']")
    titulos = driver.find_elements(By.XPATH,"//*[@class='CoreText-sc-1txzju1-0 MveHm']")

    for streamer, visualizacao, link, titulo in itertools.islice(zip(streamers, vizualizacao, links, titulos), 10):
        nome_streamer = streamer.text  # Use .get_attribute("alt") para obter o nome da imagem
        vizualizacao_streamer = visualizacao.text
        link_streamer = link.get_attribute("href")
        titulo_streamer = titulo.text

        info = {
            "Categoria": categoria,
            "Nome": nome_streamer,
            "Visualizações": vizualizacao_streamer,
            "Link": link_streamer,
            "Titulo": titulo_streamer
        }

        info_streamers.append(info.copy())
    

# Crie um DataFrame com os dados
df = pd.DataFrame(info_streamers)

def convert_to_int(visualizacao):
    num_str = ''.join(filter(str.isdigit, visualizacao))
    if 'mil' in visualizacao:
        return int(num_str) * 1000
    else:
        return int(num_str)

# Aplicar a função ao DataFrame
df['Visualizações'] = df['Visualizações'].apply(convert_to_int)


# Remover linhas com menos de 100 espectadores
df = df[df['Visualizações'] >= 100]

df = df.drop_duplicates()
df = df.sort_values('Visualizações', ascending=False)
df = df.reset_index(drop=True)

# Exportar DataFrame para um arquivo CSV
df.to_csv('Dados_Streamers.csv', sep=';', encoding='utf-8', index=False)

print(df)

# Feche o navegador
driver.quit()

