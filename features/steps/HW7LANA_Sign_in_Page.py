
from behave import then, when


@when('Click on cart icon')
def click_on_cart(context):
    context.driver.find.element().click()


@then('Verify Sign In page is opened')
def verify_sign_in_opened(context):
    context.app.sign_in_page.verify_signin_opened()


@then('Verify Shopping Cart is Empty')
def verify_empty_shopping_cart(context):
    context.driver.find.element()