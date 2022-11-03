from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.product_page import DealPage
from pages.search_results_page import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.deal_page = DealPage(self.driver)
        self.search_results = SearchResults(self.driver)
