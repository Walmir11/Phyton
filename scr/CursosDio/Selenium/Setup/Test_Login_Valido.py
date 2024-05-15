import pytest
from pages.Login_page import LoginPage
from pages.home_page import HomePage


#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_login_valido(self):
        #instanciando os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        #faz o login
        login_page.fazer_login('standard_user','secret_sauce')
        
        #verifica se o login foi realizado
        home_page.verificarLoginSucesso()
        #assert driver.find_element(By.XPATH,'//span[@class="title"]').is_displayed
