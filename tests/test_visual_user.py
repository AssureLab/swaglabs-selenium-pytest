from pages.login_page import LoginPage
from pages.visual_inventory_page import InventoryPage


def test_visual_user_ui_validation(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.load()
    login.login("visual_user", "secret_sauce")

    assert "inventory" in browser.current_url

    inventory = InventoryPage(browser)
    inventory.verify_backpack_image()
    inventory.verify_cart_icon_visual_position()
