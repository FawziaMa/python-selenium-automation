from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLER_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')
HEADER_LINKS = (By. XPATH, '//div[contains(@class, "nav-tab-all")]//li')
LINK_TITLES = (By. XPATH, '//span[contains(@class, "LandingPageBannerText")]')


@when("Open Amazon BestSellers page")
def open_bestsellers_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("User sees 5 links on page")
def links_on_page(context):
    links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(links) == 5, "Expected 5 links but got {len(links}"


@then('Clicks on each top link and verifies that correct page opens')
def header_links(context):
    all_links = context.driver.find_elements(*HEADER_LINKS)
    for i in range(len(all_links)):
        link_to_click = context.find_element(*HEADER_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()
        header_text = context.driver.find_elements(*LINK_TITLES)
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'
