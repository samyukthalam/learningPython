from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.foundit.in/seeker/registration")
driver.maximize_window()
list_of_cookies=driver.get_cookies()
for cookie in list_of_cookies:
    print(cookie)
    driver.delete_cookie(cookie)
    driver.add_cookie(cookie)