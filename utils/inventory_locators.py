from selenium.webdriver.common.by import By


class InventoryLocators:
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE_FROM_CART = (By.XPATH, "//button[text()='Remove']")
    BADGE = (By.XPATH, "//div[@id='shopping_cart_container']//span")
