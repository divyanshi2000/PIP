from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

#import Add_customer details

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
if driver.find_element(By.XPATH,"//div//button[text()='Home']").is_displayed():
   print("Home button is visible.")
else:
   print("Home button is not visible.")

if driver.find_element(By.XPATH,"//div//strong[text()='XYZ Bank']").is_displayed():
   print("XYZ Bank is visible.")
else:
   print("XYZ Bank is not visible.")
time.sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Bank Manager Login"]').click()
print("Bank Manager Login successfully")
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[1]/button[1]").click()
time.sleep(2)
print("Clicked on ADD customer successfully")
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input").send_keys("Divyanshi")
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input").send_keys("Rajput")
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input").send_keys("DR0012345")
time.sleep(2)
if driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/form/button").is_displayed():
   print("Add customer button is visible.")
else:
   print("Add customer button is not visible.")
driver.find_element(By.XPATH, value="//div//button[text()='Add Customer']").click()
time.sleep(2)
print("Customer added successfully with customer id")

time.sleep(5)