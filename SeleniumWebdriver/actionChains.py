from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")
driver.maximize_window()
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, 'APjFqb'))
actions.context_click().send_keys("Test Automation").send_keys(Keys.ENTER).perform()