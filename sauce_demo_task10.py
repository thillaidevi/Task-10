
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Edge()  # Ensure EdgeDriver is installed

# Open the website
driver.get("https://www.saucedemo.com/")

# Capture and print title and current URL
webpage_title = driver.title
webpage_url = driver.current_url
print(f"Title: {webpage_title}")
print(f"Current URL: {webpage_url}")

# Locate username and password fields, enter credentials, and login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for page to load
time.sleep(3)

# Capture the URL after login (Dashboard page)
dashboard_url = driver.current_url
print(f"Dashboard URL: {dashboard_url}")

# Extract full page content
page_content = driver.find_element(By.TAG_NAME,'body').text

# Save the webpage content into a text file

with open("Webpage_Task11.txt", "w") as file:
    file.write(page_content)

# Close the browser
driver.quit()