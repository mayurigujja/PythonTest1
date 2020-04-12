import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\mayurigu\\Downloads\\chromedriver_win32 (7)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.familysearch.org/en/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("(//button[text()='Memories'])[1]")).perform()
action.move_to_element(driver.find_element_by_xpath("(//button[text()='Memories'])[1]")).click().perform()

wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Gallery")))
action.move_to_element(driver.find_element_by_xpath("//li[@class='submenu-item ']/a[text()='Gallery']")).perform()
action.move_to_element(driver.find_element_by_xpath("//li[@class='submenu-item ']/a[text()='Gallery']")).click().perform()



