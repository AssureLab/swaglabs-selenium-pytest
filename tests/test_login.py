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
    assert "sauce-backpack-1200x1500" in src, f"Backpack image is incorrect for problem_user: {src}"


def test_glitch_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    load_time = login.login_with_timer("performance_glitch_user", "secret_sauce")

    print(f"Inventory page load time: {load_time:.2f} seconds")

    assert "inventory" in browser.current_url
    assert load_time > 2, f"Expected glitch delay, but load time was {load_time:.2f} seconds"


def test_error_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("error_user", "secret_sauce")
    assert "inventory" in browser.current_url


def test_visual_user_login(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("visual_user", "secret_sauce")

    assert "inventory" in browser.current_url

    # Locate the backpack image
    backpack_img = wait_for(browser).until(
        EC.visibility_of_element_located((LoginPageLocators.IMG_BACKPACK))
    )

    # Get its src attribute
    img_src = backpack_img.get_attribute("src")
    print(f"Image source: {img_src}")

    # Check if the image source is correct
    assert "sauce-backpack-1200x1500" in img_src, "Backpack image is incorrect for visual_user"
