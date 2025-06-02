import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver Manager Class
class WebDriverManager:
    def __init__(self):
        self.driver = webdriver.Edge()

    def open_url(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "login-button")))

    def quit_driver(self):
        self.driver.quit()

# Pytest Fixture Using WebDriverManager
@pytest.fixture
def driver_manager():
    manager = WebDriverManager()
    yield manager
    manager.quit_driver()

# Test Case: Verify Home Page Title
def test_home_page_title(driver_manager):
    driver_manager.open_url("https://www.saucedemo.com/")
    assert driver_manager.driver.title == "Swag Labs", "Home Page Title Mismatch"

# Test Case: Verify Home Page URL
def test_home_page_url(driver_manager):
    driver_manager.open_url("https://www.saucedemo.com/")
    assert driver_manager.driver.current_url == "https://www.saucedemo.com/", "Home Page URL Mismatch"

# Login Test with Parameterization
@pytest.mark.parametrize("username,password,expected_url", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("wrong_user", "wrong_password", None)
])
def test_login(driver_manager, username, password, expected_url):
    driver_manager.open_url("https://www.saucedemo.com/")
    driver = driver_manager.driver
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if expected_url:
        assert driver.current_url == expected_url, "Dashboard URL Mismatch"
    else:
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface" in error_message, "Invalid Login Test Failed"