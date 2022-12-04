from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Homework8Page(Page):
    ALL_DEPARTMENTS = (By.ID, 'searchDropdownBox')
    SELECTED_MUSIC_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="dmusic"]')
    NEW_ARRIVALS = (By.XPATH, "//a[@href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    SEARCH_BOX = (By. ID, 'twotabsearchtextbox')

    def select_department(self):
        select = Select(self.find_element(*self.ALL_DEPARTMENTS))
        select.select_by_value('search-alias=digital-music')

    def verify_department(self):
        self.wait_for_element_appear(*self.SELECTED_MUSIC_DEPARTMENT)

    def hover_new_arrivals(self):
        select_new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_new_arrivals)
        actions.perform()

    def verify_user_see_deals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS)


