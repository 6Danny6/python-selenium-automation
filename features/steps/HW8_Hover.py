from behave import given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given('Open Product Page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')


@when('Hovers over New Arrivals')
def hover_new_arrivals(context):
    context.app.homework8_page.hover_new_arrivals()


@then('Verifies that the user sees the deals')
def verify_user_see_deals(context):
    context.app.homework8_page.verify_user_see_deals()

