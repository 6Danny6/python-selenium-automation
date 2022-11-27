from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


PRIVACY_LINK =(By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def terms_and_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@given('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_open_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('Current windowS:', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))
    print('Current window:', context.driver.current_window_handle)


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    context.driver.switch_to.window(context.original_window)


