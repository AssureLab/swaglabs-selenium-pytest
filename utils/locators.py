class LoginPageLocators:
    USERNAME = "user-name"
    PASSWORD = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = ("xpath", "//h3[@data-test='error']")


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
