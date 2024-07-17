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
        botaoDetalhes = (By.ID, 'Botao_mais_detalhes_card_tempo_no_momento')
        Cidade = (By.XPATH, '(//*[@class="link"])[2]')
        selecionarCidade = (By.XPATH, '//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]')
        clima_15Dias = (By.XPATH, "//*[@id='Botao_barra_navegacao_15_dias'][@class='link actTriggerGA']")
        maisDias1 = (By.ID, "Botao_1_mais_5_dias_timeline_15_dias")
        maisDias2 = (By.ID, "Botao_2_mais_5_dias_timeline_15_dias")

        # Clicar no botão para ver mais detalhes do clima
        base_page.clicar(botaoDetalhes)
        time.sleep(2)
        
        # Clicar para selecionar a cidade
        base_page.clicar(Cidade)
        time.sleep(2)
        
        # Selecionar Lagarto, SE
        base_page.clicar(selecionarCidade)
        time.sleep(2)
        
        # Clicar para ver o clima para 15 dias
        base_page.clicar(clima_15Dias)
        time.sleep(2)

        base_page.clicar(maisDias1)
        time.sleep(2)

        base_page.clicar(maisDias2)
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

        # Exibir os dados coletados
        print(df)

        # Exibir as médias calculadas
        print(f"Média geral da temperatura: {media_temperatura:.2f}°C")
        print(f"Média geral da umidade: {media_umidade:.2f}%")

        df.to_csv('dados_clima.csv', sep=';', encoding='latin1', index=False)
