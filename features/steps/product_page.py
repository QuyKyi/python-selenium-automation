from selenium.webdriver.common.by import By
from behave import when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOL_TIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')


@when('CLick on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Select shoes size')
def select_size(context):
    context.driver.find_element(*SIZE_SELECTION_BTN).click()
    context.driver.find_element(*SIZE_OPTION_0).click()
    import time
    time.sleep(2)


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count}'
