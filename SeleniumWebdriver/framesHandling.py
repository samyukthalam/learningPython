from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_link_target")
driver.maximize_window()
current_Window=driver.current_window_handle
driver.switch_to.frame("iframeResult")
driver.find_element(By.LINK_TEXT,"Visit W3Schools.com!").click()
all_Windows=driver.window_handles
for window_handle in all_Windows:
    if current_Window != window_handle:
        driver.switch_to.window(window_handle)
        print(driver.title)
        driver.close()
        break
driver.switch_to.window(current_Window)
driver.switch_to.default_content()
print(driver.title)
driver.close()