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
t=1


driver.get('https://demoqa.com/automation-practice-form')

driver.maximize_window()
nom= driver.find_element(By.XPATH,"//input[contains(@id,'firstName')]")
nom.send_keys("Eric")
nom.send_keys(Keys.TAB + "Villanueva" + Keys.TAB + "eric.cire.vv@gmail.com")
driver.execute_script("window.scrollTo(0,500)")
driver.find_element(By.XPATH, "(//label[contains(@class,'custom-control-label')])[1]").click()
driver.find_element(By.XPATH, "//input[contains(@id,'userNumber')]").send_keys("849-406-5159")
#driver.find_element(By.CSS_SELECTOR, "//div[contains(@class,'value-container--is-multi css-1hwfws3')]").send_keys("Hola")
driver.find_element(By.XPATH,"//label[contains(text(),'Music')]").click()
driver.execute_script("window.scrollTo(0,500)")

try:
    Buscar= WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'uploadPicture')]")))
    Buscar=driver.find_element(By.XPATH,"//input[contains(@id,'uploadPicture')]")
    Buscar.send_keys("C://Users//Heriberto Villanueva//Desktop//Selenium Pythom//Imagenes//demo1.jpg")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible ")

driver.execute_script("window.scrollTo(0,200)")
time.sleep(t)
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("calle primera, casa no.3")
time.sleep(t)
wait = WebDriverWait(driver, 10)  # Cambia 'driver' por tu objeto de WebDriver

# Espera hasta que el iframe esté presente en la página
iframe = wait.until(EC.presence_of_element_located((By.ID, "google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0")))

# Cambia al iframe
driver.switch_to.frame(iframe)

# Haz clic en el botón
button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
button.click()


driver.close()

