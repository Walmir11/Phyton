import pandas as pd
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')

class Test01:
    def test_raspagem_clima_Lagarto(self):
        base_page = BasePage()

        base_page.clicar((By.ID,'Botao_mais_detalhes_card_tempo_no_momento'))
        time.sleep(2)
        base_page.clicar((By.XPATH, '//*[@itemprop="name" and text()="Cidade"]'))
        time.sleep(2)
        base_page.clicar((By.XPATH,'//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]'))
        time.sleep(2)
        base_page.clicar((By.XPATH,"//*[@id='Botao_barra_navegacao_15_dias'][@class='link actTriggerGA']"))
        time.sleep(2)

        dias = base_page.encontrarElementos((By.XPATH, '//div[@class="date-inside-circle" or @class="date-inside-circle with-alert"]'))
        tempMinMax = base_page.encontrarElementos((By.XPATH, '//span[@class="-gray"]'))
        umidMinMax = base_page.encontrarElementos((By.XPATH, '//div[@class="-gray _flex"]'))


        assert len(dias) == len(umidMinMax), "A quantidade de dias e elementos de umidade não coincide."
        assert len(tempMinMax) == len(dias) * 2, "A quantidade de elementos de temperatura não é o dobro da quantidade de dias."

        # Criar uma lista de dicionários
        dados_clima = []
        for i in range(len(dias)):
            dia = dias[i].text
            temperatura_min = tempMinMax[i * 2].text
            temperatura_max = tempMinMax[i * 2 + 1].text
            umidade_min = umidMinMax[i].find_elements_by_xpath('.//span')[0].text
            umidade_max = umidMinMax[i].find_elements_by_xpath('.//span')[1].text

            dados_clima.append({
                'dia': dia,
                'temperatura_min': temperatura_min,
                'temperatura_max': temperatura_max,
                'umidade_min': umidade_min,
                'umidade_max': umidade_max
            })

        # Exibir os dados coletados
        for dado in dados_clima:
            print(dado)
        