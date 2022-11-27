from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class AmazonMainPage(Page):
    ORDERS_INPUT = (By.ID, '#nav-orders')
    CART = (By.ID, '#nav-cart')
    ZERO = (By.ID, '#nav-cart-count')

    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def click_orders_link(self):
        self.click(*self.ORDERS_INPUT)

    def click_on_cart(self):
        self.click(*self.CART)

    def verify_shopping_cart_empty(self):
        return self.wait.until(EC.presence_of_element_located(*self.CART))


class SignInPage(Page):
    HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, "#ap_email")

    def verify_signin_is_opened(self):
        expected_text = 'Sign in'
        actual_text = self.find_element(*self.HEADER).text
        assert actual_text == expected_text, f'Expected {expected_text}'
        assert self.find_element(*self.EMAIL).is_diplayed()

        #self.verify_url_contains_query(https://www.amazon.com/ap/signin)


