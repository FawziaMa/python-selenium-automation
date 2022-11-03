from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class DealPage(Page):
    NEW_ARRIVALS_HOVER = (By. CSS_SELECTOR, "a[aria-label='New Arrivals']")
    NEW_ARRIVALS_MENU_DEALS = (By. CSS_SELECTOR, ".mega-menu")

    def open_product_page(self, product):
        self.driver.get('https://www.amazon.com/gp/product/' + product)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_HOVER)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrival_deals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_MENU_DEALS)




