from selenium  import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--headless')
driver.get("https://www.google.com")
driver.find_element(By.ID,'APjFqb').send_keys('Test Automation')
driver.find_element(By.ID,'APjFqb').send_keys(Keys.ENTER)
wait=WebDriverWait(driver,60)
wait.until(EC.title_is('Test Automation - Google Search'))

# Print all the video titles,views, posted time
searchResults = driver.find_elements(By.XPATH,"//div[@class='qGXjvb']/div")
print(len(searchResults))
for result in range(1,len(searchResults)):
    print(driver.find_element(By.XPATH,"//div[@class='qGXjvb']/div["+str(result)+"]//a[@class='sVXRqc']").text)
