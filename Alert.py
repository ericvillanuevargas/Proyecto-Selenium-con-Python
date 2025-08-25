import time

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
t=1

driver.get("https://demoqa.com/alerts")

driver.find_element(By.XPATH,"//button[contains(@id,'confirmButton')]")
time.sleep(2)
try:
    Buscar= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"el boton")))
    Buscar=driver.find_element(By.XPATH,"el botn")

except TimeoutException as ex:
    print(ex.msg)
    print("so las 11")


time.sleep(5)
driver.close()