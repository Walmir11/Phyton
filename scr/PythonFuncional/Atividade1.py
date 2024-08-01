from methods_auto import Methods_auto as ma
from time import sleep

driver = ma.start_chrome_driver(incognito=True,undetected_driver=True)

URL = 'https://www.saucedemo.com/'
sleep(2)


driver.get(URL)
