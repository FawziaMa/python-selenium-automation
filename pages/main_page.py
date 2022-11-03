from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MainPage(Page):
    SEARCH_INPUT = (By. ID, "twotabsearchtextbox")
    SEARCH_BTN = (By. ID, "nav-search-submit-button")
    DEPARTMENT_SELECTION = (By. ID, "searchDropdownBox")
    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.driver.find_element(By.XPATH, "//a[@class='nav-a nav-a-2   nav-progressive-attribute']").click()

    def click_cart_icon(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()

    def select_department(self, selection_value):
        select = Select(self.driver.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f"search-alias={selection_value}")

