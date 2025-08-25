import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
#driver.implicitly_wait(10)
t=2

driver.find_element(By.XPATH,"//span[contains(text(),'Check Box')]").click()

btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/label[1]/span[1]")))
btn.click()





time.sleep(t)
driver.close()