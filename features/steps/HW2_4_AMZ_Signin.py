from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href,'nav_orders_first')]").click()

@then('Sign in page opened')
def verify_sign_in_page_opened (context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    expected_text = 'Sign-In'
    assert expected_text == actual_text, f"Error, Expected text: '{expected_text}', but got actual text: '{actual_text}'"
