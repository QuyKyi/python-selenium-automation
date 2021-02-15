from selenium.webdriver.common.by import By
from behave import when

PRODUCT_RESULT = (By.XPATH, "//span[@data-component-type = 's-search-results']//a[.//span[@class='a-price']]")


@when('Click on the first product')
def first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()
