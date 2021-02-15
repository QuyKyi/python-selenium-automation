from selenium.webdriver.common.by import By
from behave import given, then


BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')


@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime?_encoding=UTF8&ref_=nav_cs_primelink_nonmember_241bcdc839e0440ab2c31e06680f1049')


@then('Verify {expected_boxes} benefit boxes are displayed')
def verify_boxes(context, expected_boxes):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes} boxes, but we see {len(actual_boxes)}'

