from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.visual_inventory_page import InventoryPage


def test_visual_user_ui_validation(browser, config):
    login = LoginPage(browser, config["base_url"])
    login.check_login("visual_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.verify_backpack_image()
    inventory.verify_cart_icon_visual_position()
    inventory.verify_burger_menu_visual_position()

    inventory.go_to_cart()

    cart = CartPage(browser)
    cart.verify_checkout_button_visual_position()
