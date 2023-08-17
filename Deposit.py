
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, value="//div//button[text()='Customer Login']").click()
print("Customer login sucessfully")

driver.find_element(By.XPATH, value='//*[@id="userSelect"]').click()

element=driver.find_element(By.XPATH, value='//select[@id="userSelect"]')
drp=Select(element)
drp.select_by_visible_text("Hermoine Granger")
time.sleep(2)
# Assertion for Login button visibility
login_button = driver.find_element(By.XPATH, "//div//button[text()='Login']")
assert login_button.is_displayed(), "Login button is not visible."
print("Login button is visible.")

driver.find_element(By.XPATH, value="//div//button[text()='Login']").click()
print("Login sucessfully")
time.sleep(2)

driver.find_element(By.XPATH, value="//button[contains(text(), 'Deposit')]").click()

driver.find_element(By.XPATH, value="//input[@ng-model='amount']").send_keys("1000")
print("Amount to be Deposited")
time.sleep(2)
driver.find_element(By.XPATH, value="//div//button[text()='Deposit']").click()
print("Deposit Successful")

# Assertion for Logout button visibility
logout_button = driver.find_element(By.XPATH, "//div//button[text()='Logout']")
assert logout_button.is_displayed(), "Logout button is not visible."
print("Logout button is visible.")

# Close the browser
driver.quit()
