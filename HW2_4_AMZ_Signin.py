from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/user/Documents/Automation/python-selenium-automation/chromedriver")
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH,"//a[contains(@href,'nav_orders_first')]").click()

actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
expected_text = 'Sign-In'

assert expected_text == actual_text, f'Expected [{expected_text}, but got {actual_text}'
driver.quit()