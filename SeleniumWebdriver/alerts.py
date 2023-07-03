from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm#")
driver.maximize_window()
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.NAME,"submit")).click().perform()
alertPopUp=driver.switch_to.alert
print(alertPopUp.text)
alertPopUp.accept()