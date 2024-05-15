import conftest

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrarElemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrarElementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.encontrarElemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrarElemento(locator).click()

    def verificarExistencia(self, locator):
        assert self.encontrarElemento(locator).is_displayed(),f'Elemento {locator} não foi encontrado na tela '

    def pegar_texto_elemento(self, locator):
        return self.encontrarElemento(locator).text
