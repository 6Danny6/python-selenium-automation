from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

NAVY_BUTTON = (By.ID, 'color_name_1')
COLOR_OPTION_TEXT = (By.CSS_SELECTOR, '#variation_color_name span.selection')
DIFFERENT_COLORS = (By.CSS_SELECTOR, '#variation_color_name ul li')


@given('Open Amazon product page')
def lacoste_button_down(context):
    context.driver.get('https://www.amazon.com/Lacoste-Sleeve-Button-up-Oxford-Button/dp/B09TFY8SHL')
    sleep(3)


@then('Verify user can click on image')
def verify_product_image(context):
    expected_colors = ['Blanc', 'Navy Blue/Navy Blue', 'Overview']

    actual_colors = []

    colors = context.driver.find_elements(*DIFFERENT_COLORS)
    print('Colors:', colors)
    for colors in colors:
        colors.click()
        current_color = context.driver.find_element(*COLOR_OPTION_TEXT).text
        actual_colors += [current_color]
        print(actual_colors)

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'




#