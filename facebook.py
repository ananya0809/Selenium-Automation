import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\anany\\Desktop\\FB Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
time.sleep(3)
driver.find_element(By.NAME, "firstname").send_keys("Ananya")
driver.find_element(By.NAME, "lastname").send_keys("Agrawal")
driver.find_element(By.NAME, "reg_email__").send_keys("myname@email.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("myname@email.com")
driver.find_element(By.ID, "password_step_input").send_keys("randompassword")
day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text("8")
month = Select(driver.find_element(By.NAME, "birthday_month"))
month.select_by_visible_text("Sep")
year = Select(driver.find_element(By.NAME, "birthday_year"))
year.select_by_visible_text("2001")
driver.find_element(By.XPATH, "//label[text()='Female']").click()
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
