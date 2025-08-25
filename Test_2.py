import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Cargar una página web
driver.get('https://demoqa.com/text-box')

driver.maximize_window()
nom= driver.find_element(By.ID,"userName")
nom.send_keys("Eric")
time.sleep(1)
driver.find_element(By.ID,"userEmail").send_keys("eric.cire.vv@gmail.com")
time.sleep(1)
driver.find_element(By.ID,"currentAddress").send_keys("Direccion 1")
time.sleep(1)
driver.find_element(By.ID,"permanentAddress").send_keys("Direeccion 2")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.close()