import os
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_and_remove_items(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
    inventory = InventoryPage(browser)
    inventory.add_and_remove_items()
    ss_path = os.path.join(os.getcwd(), "screenshots")
    browser.save_screenshot(os.path.join(ss_path, "add_and_remove_items.png"))