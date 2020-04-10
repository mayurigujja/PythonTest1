# Functional test on a greenkart ( e-commerce application) that performs the following tasks
# 1. Searches for a keyword
# 2. Adds veggies to the cart
# 3. Proceeds to checkout
# 4. Applies promos
# 5. Does all validations in these two pages

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\mayurigu\\Downloads\\chromedriver_win32 (7)\\chromedriver.exe")
# Global wait
driver.implicitly_wait(5)
# Navigate to the greenkart application
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# Search with "ber" keyword
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# Count the number of fruits/veggies returned
countNUM = len(driver.find_elements_by_css_selector("div.products"))
# Initialize two lists to validate the veggies name before and after checkout
VeggiesFirstPage = []
VeggiesLastPage = []
# Click on add to cart button of all the veggies in the search results
addToCartButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for btn in addToCartButtons:
    vegname = btn.find_element_by_xpath("parent::div/parent::div/h4").text
    VeggiesFirstPage.append(vegname)
    btn.click()
driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
vegTable = driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in vegTable:
    veggie = veg.text
    VeggiesLastPage.append(veggie)
print(VeggiesLastPage)
print(VeggiesFirstPage)
assert VeggiesFirstPage == VeggiesLastPage
discountBeforePromo = driver.find_element_by_class_name("discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoBtn")))
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
CodeText = driver.find_element_by_class_name("promoInfo").text
assert "Code applied" in CodeText
discountAfterPromo = driver.find_element_by_class_name("discountAmt").text
assert float(discountAfterPromo) < int(discountBeforePromo)


