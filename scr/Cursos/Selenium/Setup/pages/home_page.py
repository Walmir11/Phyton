from pages.base_page import BasePage 
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH,'//span[@class="title"]')
        self.item_inventario = (By.XPATH,"//*[@class='inventory_item_name ' and text()='{}']")
        self.botao_addCarrinho = (By.XPATH,"//*[text()='Add to cart']")
        self.iconeCarrinho = (By.XPATH,"//*[@class='shopping_cart_link']")

    def verificarLoginSucesso(self):
        self.verificarExistencia(self.titulo_pagina)

    def adicionar_ao_carrinho(self,nome_item):
        item = (self.item_inventario[0],self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_addCarrinho)

    def acessar_carrinho(self):
        self.clicar(self.iconeCarrinho)
