from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    IMG_BACKPACK = (By.CSS_SELECTOR, "img[data-test='inventory-item-sauce-labs-backpack-img']")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")


class InventoryPageLocators:
    ADD_TO_CART = "add-to-cart-sauce-labs-backpack"
    REMOVE_FROM_CART = "remove-sauce-labs-backpack"
    CART_ICON = "shopping_cart_container"


class CartPageLocators:
    CHECKOUT_BUTTON = "checkout"


class CheckoutPageLocators:
    FIRST_NAME = "first-name"
    LAST_NAME = "last-name"
    POSTAL_CODE = "postal-code"
    CONTINUE_BUTTON = "continue"
    FINISH_BUTTON = "finish"
