from selenium import webdriver
from selenium.webdriver.common.by import By

# Using Send Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.foundit.in/seeker/registration")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class='uploadResumeContent']//input").send_keys(
    "/Users/nukathoti/Downloads/Snr QA Lead Or Architect-Swathi.docx")
