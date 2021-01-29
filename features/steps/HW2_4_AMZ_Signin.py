from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

def setup_method(context):
    context.driver = webdriver.Chrome(executable_path="/Users/user/Documents/Automation/python-selenium-automation/chromedriver")
    context.driver.implicitly_wait(6)

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def click_(context):
    search_field = context.d.find_element(By.XPATH, "//a[contains(@href,'nav_orders_first')]").click()

@then('Sign in page opened')
def verify_sign_in_page_opened (context):
    actual_text = context. driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    expected_text = 'Sign-In'
    assert expected_text == actual_text, f"Error, Expected text: '{expected_text}', but got actual text: '{actual_text}'"

def teardown_method(context):
    context.driver.quit()