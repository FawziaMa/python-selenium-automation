from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
driver.get("https://www.amazon.com/")

driver.find_element(By.XPATH, "//a[@class='nav-a nav-a-2   nav-progressive-attribute']").click()

expected_result = 'Sign in', 'Email or mobile phone number'
actual_result = driver.find_element(By.XPATH, "//h1[@class= 'a-spacing-small']").text, driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']").text

assert expected_result == actual_result, f'Error: Expected {expected_result}, but got {actual_result}'

driver.quit()