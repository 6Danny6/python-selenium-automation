from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amzon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('searc for {product}')
def search_product(context, product):
    element = context.driver.find_element(by.ID, )