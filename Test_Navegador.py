import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

t=4

driver = webdriver.Chrome()

# Cargar una página web
driver.get('https://demoqa.com/text-box')

driver.maximize_window()
time.sleep(t)


driver.get('https://www.selenium.dev/documentation/webdriver/getting_started/')
time.sleep(t)

driver.get('https://tienda.claro.com.do/')
time.sleep(t)

driver.execute_script("window.history.go(2)")
time.sleep(t)



