from pages.base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):

    def empty_cart_message(self, expected_result):
        actual_result = self.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
        assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

