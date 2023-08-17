from select import select

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(20)
#import open_account

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Bank Manager Login"]').click()

print("Bank Manager Login successfully")
driver.find_element(By.XPATH, value="//button[contains(text(), 'Open Account')]").click()
time.sleep(1)
print("clicked on open account successfully")
# Verify User Select dropdown visibility
user_select_dropdown = driver.find_element(By.XPATH, '//select[@id="userSelect"]')
assert user_select_dropdown.is_displayed(), "User Select dropdown is not visible."

driver.find_element(By.XPATH, value='//*[@id="userSelect"]').click()

element=driver.find_element(By.XPATH, value='//select[@id="userSelect"]')
drp=Select(element)
drp.select_by_visible_text("Neville Longbottom")
time.sleep(1)
# Verify Currency dropdown visibility
currency_dropdown = driver.find_element(By.XPATH, '//select[@id="currency"]')
assert currency_dropdown.is_displayed(), "Currency dropdown is not visible."

driver.find_element(By.XPATH, value='//*[@id="currency"]').click()
element=driver.find_element(By.XPATH, value='//select[@id="currency"]')
time.sleep(1)
drp=Select(element)
drp.select_by_visible_text("Pound")
time.sleep(1)

# Verify Process button visibility
process_button = driver.find_element(By.XPATH, "//div//button[text()='Process']")
assert process_button.is_displayed(), "Process button is not visible."

driver.find_element(By.XPATH, value="//div//button[text()='Process']").click()
print("Account created successfully with account Number :1019")

# Close the browser
driver.quit()
