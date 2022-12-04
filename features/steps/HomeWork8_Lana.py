from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BOX = (By. ID, 'twotabsearchtextbox')


@given('Open Amazon Main Page')
def open_amazon_main_page(context):
    context.app.main_page.open_main()


@when('Select Digital Music')
def click_on_amazon_music(context):
    context.app.homework8_page.select_department()


@when('Search for {artist}')
def search_for_musical_artist(context, artist):
    element = context.driver.find_element(*SEARCH_BOX)
    element.clear()
    element.send_keys(artist)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify Music Department')
def verify_music_department(context):
    context.app.homework8_page.verify_department()
