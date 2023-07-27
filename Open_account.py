from select import select

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#import open_account

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Bank Manager Login"]').click()
time.sleep(2)
print("Bank Manager Login successfully")
driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[1]/button[2]").click()
time.sleep(2)
print("clicked on open account successfully")
driver.find_element(By.XPATH, value='//*[@id="userSelect"]').click()
time.sleep(2)
element=driver.find_element(By.XPATH, value='//select[@id="userSelect"]')
time.sleep(2)
drp=Select(element)
drp.select_by_visible_text("Neville Longbottom")
time.sleep(2)
driver.find_element(By.XPATH, value='//*[@id="currency"]').click()
time.sleep(2)
element=driver.find_element(By.XPATH, value='//select[@id="currency"]')
time.sleep(2)
drp=Select(element)
drp.select_by_visible_text("Pound")
time.sleep(2)
if driver.find_element(By.XPATH,"//div//button[text()='Process']").is_displayed():
   print("Process button is visible.")
else:
   print("Process button is not visible.")
driver.find_element(By.XPATH, value="//div//button[text()='Process']").click()
print("Account created successfully with account Number :1019")
time.sleep(5)
