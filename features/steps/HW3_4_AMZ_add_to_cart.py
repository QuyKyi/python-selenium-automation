from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_BOX = (By.CLASS_NAME, 'a-section')


@given('Open Amazon Product page')
def open_amazon_product_(context):
    context.driver.get('https://www.amazon.com/Cybovac-Sweeping-Mopping-Navigation-Self-Charging/dp/B089R3K2X6?ref_=Oct_DLandingS_D_1a997180_61&smid=A3KCM76YMC142H')


@when('Press Add to Cart Button')
def add_to_cart_btn_click(context):
    context.driver.find_element(By.ID, 'add-to-cart-button')


@then('Verify that the Product is in Shopping Cart')
def verify_product_in_sp(context):
    actual_product = context.driver.find_elements(*PRODUCT_BOX)
    assert len(actual_product) >= 1