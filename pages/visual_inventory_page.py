import pytest_check as check
from utils.wait_utils import wait_for
from utils.locators import LoginPageLocators
from utils.css_utils import get_rotation_angle
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_backpack_image(self):
        backpack_img = wait_for(self.driver).until(
            EC.visibility_of_element_located(LoginPageLocators.IMG_BACKPACK)
        )
        img_src = backpack_img.get_attribute("src")
        print(f"Backpack image src: {img_src}")
        check.is_in("sauce-backpack-1200x1500", img_src, "Backpack image is incorrect")

    def verify_cart_icon_visual_position(self):
        cart = self.driver.find_element(*LoginPageLocators.CART_ICON)

        check.equal(
            cart.value_of_css_property("top"), "10px", "Cart top position is incorrect"
        )
        check.equal(
            cart.value_of_css_property("right"),
            "20px",
            "Cart right position is incorrect",
        )

        transform = cart.value_of_css_property("transform")
        transform = get_rotation_angle(transform)
        check.is_in(
            transform, ["none", ""], f"Unexpected transform applied: {transform}"
        )
