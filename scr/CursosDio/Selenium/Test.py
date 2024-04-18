import time
from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://google.com')
time.sleep(5)

browser.find_element()
