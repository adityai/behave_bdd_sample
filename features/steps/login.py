from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

@given(u'I am on the {page} page')
def step_impl(context, page):
    driver.get("https://the-internet.herokuapp.com/" + page)

@when(u'I login with {username} and {password}')
def step_impl(context, username, password):
    username_element = driver.find_element(By.NAME, "username")
    password_element = driver.find_element(By.NAME, "password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "#login > button")
    login_button.click()

@then(u'I should see a flash message saying {message}')
def step_impl(context, message):
    flash = driver.find_element(By.CSS_SELECTOR, "#flash")
    print("------Expected: ", message)
    print("--------Actual: ", flash.text)
    assert flash.text == message

