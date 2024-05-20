import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    #run test
    yield

    #teardown
    driver.quit()
