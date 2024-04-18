import time
from selenium import webdriver

browser = webdriver.Edge()
#Acessa a url
browser.get('https://google.com')
#Maximizar a tela do browser
browser.maximize_window()
#Atualiza a página
browser.refresh()

browser.get('https://www.saucedemo.com/v1/')
time.sleep(3)
#volta para página anterior
browser.back()
time.sleep(3)
#Avançar a página
browser.forward()
time.sleep(3)
#Criar uma nova aba
browser.switch_to.new_window('tab')
time.sleep(3)
#Fecha a aba ativa no momento
browser.close()
time.sleep(3)
#Fecha o browser inteiro
browser.quit() 
