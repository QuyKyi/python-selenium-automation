from selenium.webdriver.common.by import By
from behave import then


HAM_MENU = (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    #print('FIND ELEMENT')
    #element = context.driver.find_element(*HAM_MENU)
    #print(element)
    #print(type(element))


    print('FIND ELEMENTSSSSSS')
    elements = context.driver.find_elements(*HAM_MENU)
    print(elements)
    print(type(elements))

    assert len(elements) == 1
