import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\mayurigu\\Downloads\\chromedriver_win32 (7)\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
countNUM = len(driver.find_elements_by_css_selector("div.products"))

addToCartButtons = driver.find_elements_by_css_selector("div.product-action button")
for btn in addToCartButtons:
    btn.click()
driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoBtn")))
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
CodeText = driver.find_element_by_class_name("promoInfo").text
assert "Code applied" in CodeText


