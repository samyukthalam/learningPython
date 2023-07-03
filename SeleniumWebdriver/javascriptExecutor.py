from selenium import webdriver
from selenium.webdriver.common.by import By

# Using Send Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.selenium.dev/documentation/webdriver/elements/file_upload/")
driver.maximize_window()
# to scroll till page bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# click an element
button = driver.find_element(By.LINK_TEXT,"About Selenium")
driver.execute_script("arguments[0].click();",button)
print(driver.title)
