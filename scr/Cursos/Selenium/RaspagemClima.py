import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# Configuração do WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.climatempo.com.br')

wait = WebDriverWait(driver, 30)

botaoDetalhes = (By.ID, 'Botao_mais_detalhes_card_tempo_no_momento')
Cidade = (By.XPATH, '(//*[@class="link"])[2]')
selecionarCidade = (By.XPATH, '//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]')
clima_15Dias = (By.XPATH, "//*[@id='Botao_barra_navegacao_15_dias'][@class='link actTriggerGA']")
maisDias1 = (By.ID, "Botao_1_mais_5_dias_timeline_15_dias")
maisDias2 = (By.ID, "Botao_2_mais_5_dias_timeline_15_dias")

# Clicar no botão para ver mais detalhes do clima
driver.find_element(*botaoDetalhes).click()
driver.implicitly_wait(5)
# Para atualizar a página e evitar que um possível anúncio atrapalhe a execução
driver.refresh()

# Clicar para selecionar a cidade
driver.find_element(*Cidade).click()
driver.refresh()

# Selecionar Lagarto, SE
driver.find_element(*selecionarCidade).click()
driver.refresh()

# Clicar para ver o clima para 15 dias
driver.find_element(*clima_15Dias).click()
driver.implicitly_wait(5)
driver.refresh()

# Scroll para o primeiro botão de mais dias e clicar
driver.execute_script('scrollBy(0,1000)')
wait.until(EC.element_to_be_clickable(maisDias1)).click()
driver.implicitly_wait(5)

# Scroll para o segundo botão de mais dias e clicar
driver.execute_script('scrollBy(0,2000)')
wait.until(EC.element_to_be_clickable(maisDias2)).click()
driver.implicitly_wait(5)

# Loop para expandir todos os dropdowns de dias
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
driver.implicitly_wait(5)

for i in range(2, 16):
    dropdown_arrow = (By.XPATH, f"(//span[@class='dropdown-arrow'])[{i}]")
    driver.execute_script('scrollBy(0,800)')
    wait.until(EC.element_to_be_clickable(dropdown_arrow)).click()
    # Sleep para garantir que a ação de clicar no elemento seja completada antes que o script passe para a próxima interação.
    time.sleep(1)

# Encontrar elementos de dias, temperaturas e umidades
dias = driver.find_elements(By.XPATH, '//div[@class="date-inside-circle" or @class="date-inside-circle with-alert"]')
tempMinMax = driver.find_elements(By.XPATH, '//span[@class="-gray"]')
umidMinMax = driver.find_elements(By.XPATH, '//div[@class="-gray _flex"]')

# Verificar a consistência dos dados coletados
assert len(dias) == len(umidMinMax), "A quantidade de dias e elementos de umidade não coincide."
assert len(tempMinMax) == len(dias) * 2, "A quantidade de elementos de temperatura não é o dobro da quantidade de dias."

# Criar uma lista de dicionários com os dados climáticos
dados_clima = []
for i in range(len(dias)):
    dia = dias[i].text
    temperatura_min_text = tempMinMax[i * 2].text.replace('°', '').strip()
    temperatura_max_text = tempMinMax[i * 2 + 1].text.replace('°', '').strip()
    
    # Verificar se o texto não está vazio antes de converter
    temperatura_min = float(temperatura_min_text) if temperatura_min_text else 0.0
    temperatura_max = float(temperatura_max_text) if temperatura_max_text else 0.0
    
    spans = umidMinMax[i].find_elements(By.XPATH, ".//span")
    umidade_min_text = spans[0].text.replace('%', '').strip()
    umidade_max_text = spans[1].text.replace('%', '').strip()

    umidade_min = float(umidade_min_text) if umidade_min_text else 0.0
    umidade_max = float(umidade_max_text) if umidade_max_text else 0.0

    dados_clima.append({
        'dia': dia,
        'temperatura_min': temperatura_min,
        'temperatura_max': temperatura_max,
        'umidade_min': umidade_min,
        'umidade_max': umidade_max
    })

# Criar um DataFrame com os dados
df = pd.DataFrame(dados_clima)

# Calcular as médias
df['media_temperatura'] = (df['temperatura_min'] + df['temperatura_max']) / 2
df['media_umidade'] = (df['umidade_min'] + df['umidade_max']) / 2

media_temperatura = df['media_temperatura'].mean()
media_umidade = df['media_umidade'].mean()

# Exibir as médias calculadas
print(f"Média geral da temperatura: {media_temperatura:.2f}°C")
print(f"Média geral da umidade: {media_umidade:.2f}%")

# Salvar os dados em um arquivo CSV
df.to_csv('dados_clima.csv', sep=';', encoding='latin1', index=False)
print("Dados climáticos salvos em 'dados_clima.csv'.")

# Fechar o navegador
driver.quit()
