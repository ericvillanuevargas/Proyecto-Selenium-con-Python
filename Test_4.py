import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Cargar una página web
driver.get('https://tienda.claro.com.do/')

driver.maximize_window()

driver.find_element(By.XPATH,"//span[contains(text(),'account_circle')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@id='header-customer-login']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("Eric_Villanueva")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Evv191102")
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'Acceder')]").click()
input("Presiona Enter para salir...")

# Cerrar el navegador al presionar Enter
driver.quit()

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)


driver.close()