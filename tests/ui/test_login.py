import os
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    assert "invetory" in driver.current_url, "Login failed or user not redirected properly"
    ss_path = os.path.join(os.getcwd(), "screenshots")
    driver.save_screenshot(os.path.join(ss_path, "login_success.png"))