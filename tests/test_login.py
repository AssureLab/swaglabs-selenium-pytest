import os
from pages.login_page import LoginPage
from utils.locators import LoginPageLocators
from pages.visual_inventory_page import InventoryPage


def test_login_valid(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("standard_user", "secret_sauce")
    ss_path = os.path.join(os.getcwd(), "screenshots")
    browser.save_screenshot(os.path.join(ss_path, "login_success.png"))


def test_login_invalid(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("invaliduser", "secret_sauce")


def test_locked_out_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("locked_out_user", "secret_sauce")


def test_problem_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("problem_user", "secret_sauce")

    # inventory = InventoryPage(browser)
    # inventory.verify_all_product_images()


def test_glitch_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("performance_glitch_user", "secret_sauce")


def test_error_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("error_user", "secret_sauce")


def test_visual_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("visual_user", "secret_sauce")
