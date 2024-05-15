from pages.base_page import BasePage 
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH,'//span[@class="title"]')

    def verificarLoginSucesso(self):
        self.verificarExistencia(self.titulo_pagina)