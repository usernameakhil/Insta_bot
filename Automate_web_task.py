from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup your dummy credentials here
USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"

# Start the browser
driver = webdriver.Chrome()  # or use the full path to chromedriver
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Login
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(7)

# Search for cbitosc
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("cbitosc")
time.sleep(3)
search_box.send_keys(Keys.DOWN)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Follow if not already followed
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    time.sleep(2)
except:
    print("Already following or follow button not found.")

# Scrape bio and save it
try:
    bio_element = driver.find_element(By.XPATH, "//div[@class='_aacl _aacp _aacu _aacx _aad6']")
    bio_text = bio_element.text
except:
    bio_text = "Bio not found or structure changed."

# Save to file
with open("cbitosc_info.txt", "w", encoding="utf-8") as f:
    f.write("CBIT Open Source Club Bio:\n")
    f.write(bio_text)

# Done
print("✅ Info saved to cbitosc_info.txt")
driver.quit()
