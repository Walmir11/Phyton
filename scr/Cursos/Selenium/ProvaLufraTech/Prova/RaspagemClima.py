import conftest
import pandas as pd
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')

class Test01:
    def test_raspagem_clima_Lagarto(self):
        driver = conftest.driver
        base_page = BasePage()

        base_page.clicar((By.ID,'Botao_mais_detalhes_card_tempo_no_momento'))
        time.sleep(2)
        base_page.clicar((By.XPATH, '//*[@itemprop="name" and text()="Cidade"]'))
        time.sleep(2)
        base_page.clicar((By.XPATH,'//*[@class="-gray _flex _margin-b-10" and contains(text(), "Lagarto, SE")]'))
        time.sleep(2)
        