import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://tienda.claro.com.do/sx/consulta-tu-disponibilidad/internet-fijo-residencial")
driver.maximize_window()
driver.implicitly_wait(10)
t=2
#driver.execute_script("window.scrollTo(0,300)")
#driver.find_element(By.XPATH,"//span[contains(text(),'Check Box')]").click()



provincia=Select(driver.find_element(By.ID, "provincia"))
provincia.select_by_index(5)
#diasSelect=driver.find_element(By.XPATH,"//select[@id='provincia']")

#ds=Select(diasSelect)

#ds.select_by_visible_text("DUARTE")
#time.sleep(t)




time.sleep(t)
driver.close()