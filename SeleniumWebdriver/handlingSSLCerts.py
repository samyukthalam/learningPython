from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Firefox
firefox_Options=Options()
firefox_Options.add_argument('--ignore-certificate-errors')
driver=webdriver.Firefox(options=firefox_Options)
driver.get('https://cacert.org/')
driver.close()

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://cacert.org/')

safari_options = Options()
safari_options.add_argument('--ignore-certificate-errors')
driver=webdriver.Safari(options=safari_options)
driver.get('https://cacert.org/')

