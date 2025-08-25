import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Cargar una página web
driver.get('https://demoqa.com/text-box')

driver.implicitly_wait(10)
t=1


driver.maximize_window()
nom= driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys("Eric")
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("eric.cire.vv@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]").send_keys("Direccion t")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]").send_keys("Direeccion 2")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").send_keys("Direccion t")
time.sleep(2)
driver.close()