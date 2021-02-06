from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel order into Amazon Search Help Library field')
def input_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)


@then('Cancel Items or Orders text is present')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_text = "Cancel Items or Orders"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'