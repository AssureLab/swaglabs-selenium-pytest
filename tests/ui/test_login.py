import pytest
import pytest_html
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

os.makedirs("screenshots", exist_ok=True)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    assert "inventory" in driver.current_url, "Login failed or user not redirected properly"
    ss_path = os.path.join(os.getcwd(), "screenshots")
    driver.save_screenshot(os.path.join(ss_path, "login_success.png"))