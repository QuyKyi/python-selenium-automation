from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://amazon.com/')


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(search_query)


@when('Click on Amazon search icon')
def click_search_amazon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


@then('Product results for {result_word} are shown on Amazon')
def verify_search_result(context, result_word):
    actual_text = context.driver.find_element(*RESULT).text
    expected_text = f'{result_word}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    assert query in context.driver.current_url, f'Watches not in {context.driver.current_url}'

@given('Open Dress {productid} page')
def open_amazon_page(context, productid):
    context.driver.get('https://amazon.com/gp/product')