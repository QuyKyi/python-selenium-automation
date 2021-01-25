from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Users/user/Documents/Automation/python-selenium-automation/chromedriver")
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.XPATH, "//input[@type='search']")
search_field.send_keys('Cancel order')

from selenium.webdriver.common.keys import Keys

driver.find_element(By.XPATH, "//input[@type='search']").send_keys(Keys.ENTER)

content=driver.page_source
if content.find("Cancel Items or Orders"):
    print(" Cancel Items or Orders text is present in the webpage")

driver.quit()