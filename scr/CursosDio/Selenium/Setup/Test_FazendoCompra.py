import time
import pytest
from selenium.webdriver.common.by import By
import conftest

#Chama o setup que está na Conftest
@pytest.mark.usefixtures('setup_teardown')
#para chamar o específico
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        driver.find_element(By.ID,'password').send_keys('secret_sauce')
        driver.find_element(By.ID,'login-button').click()
        
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
        driver.find_element(By.ID,'back-to-products').click()
        
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH,"//*[@class='shopping_cart_link']").click()
        driver.find_element(By.ID,'checkout').click()
        driver.find_element(By.ID,'first-name').send_keys('Walmir')
        driver.find_element(By.ID,'last-name').send_keys('Neto')
        driver.find_element(By.ID,'postal-code').send_keys('49400000')
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@type='submit']").click()
        driver.find_element(By.ID,'finish').click()
        time.sleep(3)
