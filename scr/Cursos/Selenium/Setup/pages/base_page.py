import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

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
        self.esperar_elemento_aparecer(locator)
        return self.encontrarElemento(locator).text
    
    def esperar_elemento_aparecer(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verificar_elemento_existe(self,locator):
        assert self.encontrarElemento(locator),f'O elemento {locator} não existe'

    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrarElementos(locator) == 0),f'Elemento {locator} existe'

    def clique_duplo(self,locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_botao_direito(self,locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()
