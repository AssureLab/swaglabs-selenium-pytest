from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.visual_inventory_page import InventoryPage


def check_login(browser, config, user):
    login = LoginPage(browser, config["base_url"])
    login.check_login(user, "secret_sauce")


def check_inventory_page_ui_validation(inventory):
    inventory.verify_all_product_images()
    inventory.verify_cart_icon_visual_position()
    inventory.verify_burger_menu_visual_position()


def check_cart_page_ui_validation(browser):
    cart = CartPage(browser)
    cart.verify_checkout_button_visual_position()


def test_standard_user_inventory(browser, config):
    check_login(browser, config, "standard_user")
    inventory = InventoryPage(browser)
    check_inventory_page_ui_validation(inventory)
    inventory.add_and_remove_items()

    inventory.go_to_cart()
    check_cart_page_ui_validation(browser)


def test_visual_user_inventory(browser, config):
    check_login(browser, config, "visual_user")
    inventory = InventoryPage(browser)
    check_inventory_page_ui_validation(inventory)

    inventory.go_to_cart()
    check_cart_page_ui_validation(browser)
