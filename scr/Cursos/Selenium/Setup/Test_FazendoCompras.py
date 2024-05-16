import time
import pytest
from selenium.webdriver.common.by import By
from pages.Login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage
import conftest

#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
#para chamar o específico
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        produto1 = 'Sauce Labs Backpack'
        produto2 = 'Sauce Labs Bike Light'

        #Fazer login
        login_page.fazer_login('standard_user','secret_sauce')

        #Adicionando ao carrinho
        home_page.adicionar_ao_carrinho(produto1)
        time.sleep(2)
        #Verificando se está no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        time.sleep(2)

        #Voltando para fazer outra compra
        carrinho_page.clicar_continuar_comprando()
        
        home_page.adicionar_ao_carrinho(produto2)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto2)
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        
        home_page.acessar_carrinho()
        driver.find_element(By.ID,'checkout').click()
        driver.find_element(By.ID,'first-name').send_keys('Walmir')
        driver.find_element(By.ID,'last-name').send_keys('Neto')
        driver.find_element(By.ID,'postal-code').send_keys('49400000')
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@type='submit']").click()
        driver.find_element(By.ID,'finish').click()
        time.sleep(3)
