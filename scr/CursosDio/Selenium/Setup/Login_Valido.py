import pytest
import time
from Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By
import conftest

#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver

        login_page = LoginPage()

        login_page.fazer_login('standard_user','secret_sauce')
        #driver.find_element(By.ID,'user-name').send_keys('standard_user')
        #driver.find_element(By.ID,'password').send_keys('secret_sauce')
        #driver.find_element(By.ID,'login-button').click()


        assert driver.find_element(By.XPATH,'//span[@class="title"]').is_displayed
        time.sleep(2)