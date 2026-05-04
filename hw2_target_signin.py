import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# opening chrome
driver = webdriver.Chrome()
driver.maximize_window()

# open target.com
driver.get("https://www.target.com/")

# page loading
time.sleep(3)

# click account button
account_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Account')]")
account_button.click()

time.sleep(3)

# click sign in
sign_in_menu_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in or create account')]")
sign_in_menu_button.send_keys(Keys.ENTER)

time.sleep(3)

# verify sign in or create account text is shown
sign_in_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in or create account')]")
print(sign_in_text.text)

# verify sign in button is shown
sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
print(sign_in_button.is_displayed())

# browser close
driver.quit()