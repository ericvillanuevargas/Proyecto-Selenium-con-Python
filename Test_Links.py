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


driver.get('https://demoqa.com/links')
driver.maximize_window()
time.sleep(t)


links=driver.find_elements(By.TAG_NAME,"a")
print("El numero de links que hay en la pagina es: ",len(links))

for num in links:
    print(num.text)


driver.execute_script("window.scrollTo(0,100)")
driver.find_element(By.LINK_TEXT,"Home").click()

time.sleep(5)

driver.close()

