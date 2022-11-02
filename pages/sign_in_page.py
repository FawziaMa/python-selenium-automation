from pages.base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):

    def verify_sign_in_opened(self):
        self.driver.wait.until(EC.url_contains('ap/signin'))

