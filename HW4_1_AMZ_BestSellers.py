from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/user/Documents/Automation/python-selenium-automation/chromedriver")
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

BEST_SELLERS_LINKS = (By.XPATH, "//a[contains(@href,'ref=zg_bs_tab')]")

actual_elements = driver.find_elements(*BEST_SELLERS_LINKS)

assert len(actual_elements) == 5, f'Expected 5 elements, but we see {len(actual_elements)}'

driver.quit()
