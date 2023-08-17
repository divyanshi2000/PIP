from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

#import Add_customer details

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
# Assertions for Home button
home_button = driver.find_element(By.XPATH, "//div//button[text()='Home']")
assert home_button.is_displayed(), "Home button is not visible."
print("Home button is visible.")

# Assertions for XYZ Bank
xyz_bank = driver.find_element(By.XPATH, "//div//strong[text()='XYZ Bank']")
assert xyz_bank.is_displayed(), "XYZ Bank is not visible."
print("XYZ Bank is visible.")
driver.find_element(By.XPATH, value='//button[text()="Bank Manager Login"]').click()
print("Bank Manager Login successfully")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, value="//button[contains(text(), 'Add Customer')]").click()

print("Clicked on ADD customer successfully")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, value="//input[@type='text']").send_keys("Divyanshi")

driver.find_element(By.XPATH, value="//input[@placeholder='Last Name']").send_keys("Rajput")

driver.find_element(By.XPATH, value="//input[@placeholder='Post Code']").send_keys("DR0012345")

# Assertions for Add Customer button
add_customer_button = driver.find_element(By.XPATH, "//div//button[text()='Add Customer']")
assert add_customer_button.is_displayed(), "Add Customer button is not visible."
print("Add Customer button is visible.")
driver.find_element(By.XPATH, value="//div//button[text()='Add Customer']").click()
time.sleep(2)
print("Customer added successfully with customer id")

# Close the browser
driver.quit()
