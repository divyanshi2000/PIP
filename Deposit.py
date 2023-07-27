
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, value="//div//button[text()='Customer Login']").click()
print("Customer login sucessfully")
time.sleep(2)
driver.find_element(By.XPATH, value='//*[@id="userSelect"]').click()
time.sleep(2)
element=driver.find_element(By.XPATH, value='//select[@id="userSelect"]')
drp=Select(element)
drp.select_by_visible_text("Hermoine Granger")
time.sleep(2)
if driver.find_element(By.XPATH,"//div//button[text()='Login']").is_displayed():
   print("Login button is visible.")
else:
   print("Login button is not visible.")
driver.find_element(By.XPATH, value="//div//button[text()='Login']").click()
print("Login sucessfully")
time.sleep(2)

driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[3]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys("1000")
print("Amount to be Deposited")
time.sleep(2)
driver.find_element(By.XPATH, value="//div//button[text()='Deposit']").click()
print("Deposit Successful")
if driver.find_element(By.XPATH,"//div//button[text()='Logout']").is_displayed():
   print("Logout button is visible.")
else:
   print("Logout button is not visible.")
time.sleep(5)
