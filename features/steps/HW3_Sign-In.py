from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Type email on Sign-In')
def type_email(context):
    context.driver.find_element(By.XPATH,"//a[@id='nav-orders']").click()
    context.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Limitless369@outlook.com")

@then('Show email on Sign-In')
def verify_typed_email(context):
    context.expected_result = "Limitless369@outlook.com"
  #  context.actual_result = context.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Limitless369@outlook.com")
