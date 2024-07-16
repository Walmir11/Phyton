import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.button = (By.ID, 'login-button')
        self.error_message_login = (By.XPATH,"//*[@data-test='error']")
        

    def fazer_login(self, usuario, senha):
        #self.driver.find_element(*self.username).send_keys(usuario)
        #self.driver.find_element(*self.password).send_keys(senha)
        #self.driver.find_element(*self.button).click()
        self.escrever(self.username,usuario)
        self.escrever(self.password,senha)
        self.clicar(self.button)

    def verificar_mensagem_erro_login_existe(self):
        self.verificarExistencia(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self,texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f'O texto retornado foi "{texto_encontrado}", mas era esperado o texto "{texto_esperado}"'
