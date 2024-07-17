import pytest
import pandas as pd
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

# Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
class Test01:
    def test_raspagem_clima_Lagarto(self):
        base_page = BasePage()

        # Clicar no botão para ver mais detalhes do clima
        base_page.clicar((By.ID, 'Botao_mais_detalhes_card_tempo_no_momento'))
        time.sleep(2)
        
        # Clicar para selecionar a cidade
        base_page.clicar((By.XPATH, '//*[@itemprop="name" and text()="Cidade"]'))
        time.sleep(2)
        
        # Selecionar Lagarto, SE
        base_page.clicar((By.XPATH, '//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]'))
        time.sleep(2)
        
        # Clicar para ver o clima para 15 dias
        base_page.clicar((By.XPATH, "//*[@id='Botao_barra_navegacao_15_dias'][@class='link actTriggerGA']"))
        time.sleep(2)

        # Encontrar elementos de dias, temperaturas e umidades
        dias = base_page.encontrarElementos((By.XPATH, '//div[@class="date-inside-circle" or @class="date-inside-circle with-alert"]'))
        tempMinMax = base_page.encontrarElementos((By.XPATH, '//span[@class="-gray"]'))
        umidMinMax = base_page.encontrarElementos((By.XPATH, '//div[@class="-gray _flex"]'))

        # Verificar a consistência dos dados coletados
        assert len(dias) == len(umidMinMax), "A quantidade de dias e elementos de umidade não coincide."
        assert len(tempMinMax) == len(dias) * 2, "A quantidade de elementos de temperatura não é o dobro da quantidade de dias."

        # Criar uma lista de dicionários com os dados climáticos
        dados_clima = []
        for i in range(len(dias)):
            dia = dias[i].text
            temperatura_min = tempMinMax[i * 2].text
            temperatura_max = tempMinMax[i * 2 + 1].text
            spans = umidMinMax[i].find_elements(By.XPATH, ".//span")
            umidade_min = spans[0].text
            umidade_max = spans[1].text

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

        # Exibir os dados coletados
        print(df)

        # Exibir as médias calculadas
        print(f"Média geral da temperatura: {media_temperatura:.2f}°C")
        print(f"Média geral da umidade: {media_umidade:.2f}%")

        df.to_csv('dados_clima.csv', sep=';', encoding='latin1', index=False)
        