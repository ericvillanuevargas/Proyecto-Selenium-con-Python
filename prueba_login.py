import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
t=1

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()
        t = 1

   #login completo
    def test1(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        user=driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        user.send_keys("standard_user")
        password=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        btn_login.click()

        time.sleep(3)

    # login faltando el username

    def test2(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        user=driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        user.send_keys("")
        password=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        btn_login.click()
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)

        time.sleep(3)

    # login faltando el password
    def test3(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        user=driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        user.send_keys("standard_user")
        password=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        password.send_keys("")
        btn_login=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        btn_login.click()
        time.sleep(3)

    # login incompleto
    def test4(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        user=driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        user.send_keys("erir")
        password=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        password.send_keys("ddddd")
        btn_login=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        btn_login.click()
        time.sleep(3)

    def tearDown(self):
        driver= self.driver
        driver.close()

if __name__ =='__main__':
    unittest.main()