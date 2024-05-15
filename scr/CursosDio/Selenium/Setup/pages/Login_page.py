import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.button = (By.ID, 'login-button')
        

    def fazer_login(self, usuario, senha):
        #self.driver.find_element(*self.username).send_keys(usuario)
        #self.driver.find_element(*self.password).send_keys(senha)
        #self.driver.find_element(*self.button).click()
        self.escrever(self.username,usuario)
        self.escrever(self.password,senha)
        self.clicar(self.button)
