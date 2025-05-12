import os
from utils.wait_utils import wait_for
from pages.login_page import LoginPage
from utils.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


def test_login_valid(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
    ss_path = os.path.join(os.getcwd(), "screenshots")
    browser.save_screenshot(os.path.join(ss_path, "login_success.png"))


def check_error_massage(browser):
    error = wait_for(browser).until(
        EC.visibility_of_element_located((LoginPageLocators.ERROR_MESSAGE))
    )
    return error.text.lower()


def test_login_invalid(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("invaliduser", "secret_sauce")

    assert (
        "username and password do not match any user in this service"
        in check_error_massage(browser)
    )


def test_locked_out_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in check_error_massage(browser)


def test_problem_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("problem_user", "secret_sauce")
    assert "inventory" in browser.current_url

    img = wait_for(browser).until(EC.visibility_of_element_located((LoginPageLocators.IMG_BACKPACK)))
    src = img.get_attribute("src")
    assert not "sauce-backpack-1200x1500" in src, f"Unexpected src: {src}"
