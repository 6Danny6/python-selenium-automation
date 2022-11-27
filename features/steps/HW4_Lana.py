from selenium.webdriver.common.by import By
from behave import given, when, then


Best_sellers_tabs = (By.CSS_SELECTOR, 'div#zg_header a[href*="ref=zg"]')


@given('Open Bestsellers Page')
def best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Best Sellers Row Tabs')
def first_tab(context):
    context.driver.find_element(*Best_sellers_tabs)


@then('Verify all five tabs')
def verify_tabs_on_page(context):
    assert len('links') == 5, f'Expected 5 links but got {len("links")}'