from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

Sign_IN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')
Color_Options = (By.CSS_SELECTOR)

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on button from SignIn popup')
def click_sign_in(context):
   e = context.driver.wait(EC.element_to_be_clickable(*Sign_IN), message='Sign in not clickable')
   e.click()  #<-Varible                 #If Sign_IN is not clickable you can write message


@then('Verify Sign In page opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message ='Signin URL did not open')

@then('Verify user can click through')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Solid Black']

    actual_colors = []

    colors = context.driver.find_elements(*Color_Options)