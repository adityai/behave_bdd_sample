from selenium.webdriver.common.by import By
from behave import given, when, then

@given(u'I am on the {page} page')
def step_impl(context, page):
    context.driver.get("https://the-internet.herokuapp.com/" + page)

@when(u'I login with {username} and {password}')
def step_impl(context, username, password):
    username_element = context.driver.find_element(By.NAME, "username")
    password_element = context.driver.find_element(By.NAME, "password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    login_button = context.driver.find_element(By.CSS_SELECTOR, "#login > button")
    login_button.click()

@then(u'I should see a flash message saying {message}')
def step_impl(context, message):
    flash = context.driver.find_element(By.CSS_SELECTOR, "#flash")
    print("------Expected: ", message)
    print("--------Actual: ", flash.text)
    assert flash.text == message

