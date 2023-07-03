from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable--extentions')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
#chrome_options.headless = True # also works
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/intl/en_ca/chrome/update/")
print(driver.title)
