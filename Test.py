from datetime import time

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
if driver.find_element(By.XPATH,"//div//button[text()='Home']").is_displayed():
   print("Home button is visible.")
else:
   print("Home button is not visible.")

if driver.find_element(By.XPATH,"//div//strong[text()='XYZ Bank']").is_displayed():
   print("Element is visible.")
else:
   print("Element is not visible.")




