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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,300)")

btn=driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")

if(btn.is_enabled()==True):
    print("Puedes dar click")
else:
    print("No Puedes dar click")

time.sleep(5)
driver.close()