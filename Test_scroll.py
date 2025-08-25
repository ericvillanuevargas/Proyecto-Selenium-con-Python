import time

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://pixabay.com/")
driver.maximize_window()
driver.implicitly_wait(10)
t=2



try:
    Buscar= WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Discover more')]")))
    Buscar=driver.find_element(By.XPATH,"//span[@class='label--Ngqjq'][contains(.,'Discover more')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible ")



time.sleep(t)
driver.close()