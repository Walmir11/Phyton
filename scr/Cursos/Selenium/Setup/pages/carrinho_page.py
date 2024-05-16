import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH,"//*[@class='inventory_item_name' and text()='{}']")
        self.Butto_continue_comprando = (By.ID,'continue-shopping')

    def verificar_produto_carrinho_existe(self,nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificarExistencia(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.Butto_continue_comprando)