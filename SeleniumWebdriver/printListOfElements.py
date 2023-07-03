
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.google.com/search')
driver.maximize_window()
driver.find_element(By.ID,'APjFqb').send_keys('Test Automation')
wait = WebDriverWait(driver,60)
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@jsname='bw4e9b']/li")))
listOfElements=driver.find_elements(By.XPATH,"//ul[@jsname='bw4e9b']/li")
for element in listOfElements:
    print(element.text)