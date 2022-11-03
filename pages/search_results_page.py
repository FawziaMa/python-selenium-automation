from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SELECTED_DEPARTMENT = (By. CSS_SELECTOR, "#nav-subnav[data-category='{DEPARTMENT}']")

    def get_department_locator(self, department: str):
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace('{DEPARTMENT}', department)]

    def verify_department(self, department):
        department_locator = self.get_department_locator(department)
        self.wait_for_element_appear(*department_locator)

