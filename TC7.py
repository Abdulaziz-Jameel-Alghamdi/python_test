# Task 7: GitHub URL of features/steps/web_steps.py showing the code snippets of the step definitions (4 pts)

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Example: Using Selenium WebDriver for web automation#
@given('I have navigated to the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize WebDriver (Chrome in this case)
    context.driver.get("http://localhost:8000")  # Replace with your application's URL
    time.sleep(2)  # Example: Wait for page to load
#
@when('I click on the login button')
def step_impl(context):
    login_button = context.driver.find_element_by_id('login_button')  # Example: Locate login button element
    login_button.click()

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_field = context.driver.find_element_by_id('username')  # Example: Locate username input field
    password_field = context.driver.find_element_by_id('password')  # Example: Locate password input field
    username_field.send_keys(username)
    password_field.send_keys(password)

@when('I submit the login form')
def step_impl(context):
    login_form = context.driver.find_element_by_id('login_form')  # Example: Locate login form element
    login_form.submit()
    time.sleep(2)  # Example: Wait for login process (not ideal, use explicit waits in practice)

@then('I should see the dashboard page')
def step_impl(context):
    assert context.driver.current_url == 'http://localhost:8000/dashboard'  # Example: Verify dashboard URL
    # Example: Add more assertions or verification steps as needed

@then('I should see an error message')
def step_impl(context):
    error_message = context.driver.find_element_by_id('error_message')  # Example: Locate error message element
    assert error_message.is_displayed()
    # Example: Verify error message text or additional assertions

@then('I close the browser')
def step_impl(context):
    context.driver.quit()  # Close WebDriver after all scenarios

#