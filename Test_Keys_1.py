import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Cargar una página web
driver.get('https://demoqa.com/text-box')

driver.maximize_window()
nom= driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys("Eric")
nom.send_keys(Keys.TAB + "eric.cire.vv@gmail.com" + Keys.TAB + "Direccion 1" + Keys.TAB + "Direeccion 2" +Keys.TAB+Keys.ENTER)

driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").send_keys("Direccion 1")
time.sleep(2)

driver.find_element(By.XPATH,"//span[contains(text(),'Check Box')]").click()
driver.close()