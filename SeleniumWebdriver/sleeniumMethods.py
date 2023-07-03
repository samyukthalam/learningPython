from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()
assert driver.title == "ParaBank | Welcome | Online Banking"
print(driver.page_source)
print(driver.current_url)
print(driver.get_window_size())


driver.find_element(By.NAME, "username").send_keys('swathinukathoti')
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys('swathinukathoti')
driver.find_element(By.NAME, "password").send_keys('Simple*1234')
print(driver.find_element(By.XPATH, "//input[@value='Log In']").get_attribute('value'))
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
driver.find_element(By.LINK_TEXT,"Log Out").click()

driver.refresh()
driver.get('https://www.google.com')
driver.forward()
driver.back()