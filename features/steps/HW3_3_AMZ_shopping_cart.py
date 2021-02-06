from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the cart icon')
def click_on_the_cart_icon(context):
    context.driver.find_element_by_css_selector("span.nav-cart-icon.nav-sprite").click()


@then('Your Shopping Cart is empty')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = "Your Amazon Cart is empty"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'