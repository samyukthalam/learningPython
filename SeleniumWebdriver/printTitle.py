from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.google.com')
driver.maximize_window()
print(driver.title)

driver=webdriver.Firefox()
driver.get('https://www.google.com')
driver.maximize_window()

driver=webdriver.Safari()
driver.get('https://www.google.com')
driver.maximize_window()

driver.quit()