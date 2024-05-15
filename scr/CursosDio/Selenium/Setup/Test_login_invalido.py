import pytest
from pages.Login_page import LoginPage
from pages.home_page import HomePage


#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_login_valido(self):
        mensagem_erro_esperada = 'Epic sadface: Username and password do not match any user in this service'

        #instanciando os objetos a serem usados no teste
        login_page = LoginPage()

        #faz o login
        login_page.fazer_login('standard_user','senha_incorreta')
        
        #verifica se o erro apareceu
        login_page.verificar_mensagem_erro_login_existe()

        #verifica texto mensagem de erro
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)
