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

driver.get("https://demoqa.com/")
driver.maximize_window()

titulo=driver.find_element(By.XPATH,"//header/a[1]/img[1]")

print(titulo.is_displayed())

btn1=driver.find_element(By.XPATH,"(//div[contains(@class,'card-up')])[1]")


if(titulo.is_displayed()==True):
    print("Existo la imagen")
    driver.execute_script("window.scrollTo(0,100)")
    btn1.click()
    time.sleep(3)
else:
    print("No existe la imagen")
time.sleep(5)
driver.close()