from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
drpdwn_list=Select(driver.find_element(By.NAME, "country"))
for option in drpdwn_list.options:
    print(option.text)

drpdwn_list.select_by_index(10)
print(drpdwn_list.first_selected_option.text)

drpdwn_list.select_by_value('INDIA')
print(drpdwn_list.first_selected_option.text)

drpdwn_list.select_by_visible_text('KUWAIT')
print(drpdwn_list.first_selected_option.text)