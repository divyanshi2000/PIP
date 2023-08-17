from datetime import time

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(2)
# Verify Home button visibility
home_button = driver.find_element(By.XPATH, "//div//button[text()='Home']")
assert home_button.is_displayed(), "Home button is not visible."
print("Home button is visible.")

# Verify XYZ Bank element visibility
xyz_bank_element = driver.find_element(By.XPATH, "//div//strong[text()='XYZ Bank']")
assert xyz_bank_element.is_displayed(), "XYZ Bank element is not visible."
print("XYZ Bank element is visible.")

# Close the browser
driver.quit()



