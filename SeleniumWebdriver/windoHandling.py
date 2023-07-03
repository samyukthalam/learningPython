from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
currentWindow=driver.current_window_handle
print(currentWindow)
driver.find_element(By.LINK_TEXT,"Click Here").click()
listOfwindows=driver.window_handles
print(len(listOfwindows))
for handle in listOfwindows:
    if handle!=currentWindow:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.close()