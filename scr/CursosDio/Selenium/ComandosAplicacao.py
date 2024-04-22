import time
from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://saucedemo.com')
#Printa o título da página(Title)
print(f'O títolo da página é {browser.title}')
print()
#Retorna a URL da página
print(f'A URL da página é {browser.current_url}')
print()
#Retorna o código fonte
print(f'O código fonte da página é {browser.page_source}')
