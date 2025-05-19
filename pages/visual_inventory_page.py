import pytest_check as check
from utils.image_src import ImageSrc
from utils.wait_utils import wait_for
from utils.locators import LoginPageLocators
from utils.css_utils import get_rotation_angle
from utils.inventory_locators import InventoryLocators
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_all_product_images(self):
        item_images = self.driver.find_elements(*LoginPageLocators.ITEM_IMAGES)
        expected_images = (
            ImageSrc.IMAGES.items()
        )  # returns list of (name, expected_substring)

        for item_img, (name, expected_src) in zip(item_images, expected_images):
            img_src = item_img.get_attribute("src")
            print(f"{name} image src: {img_src}")
            check.is_in(expected_src, img_src, f"{name} image is incorrect: {img_src}")

    def verify_transform(self, locator, element):
        transform = locator.value_of_css_property("transform")

        if transform not in (None, "", "none"):
            angle = get_rotation_angle(transform)
            check.equal(
                angle,
                0,
                f"Unexpected transform rotation: {angle}° applied to {element}",
            )

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

        self.verify_transform(cart, "Cart Icon")

    def verify_burger_menu_visual_position(self):
        menu = self.driver.find_element(*LoginPageLocators.BURGER_MENU)
        self.verify_transform(menu, "Berger Menu")

    def add_and_remove_items(self):
        add_list = self.driver.find_elements(*InventoryLocators.ADD_TO_CART)
        for add in add_list:
            add.click()
            badge = self.driver.find_element(*InventoryLocators.BADGE)
            assert "1" == badge.text
            self.driver.find_element(*InventoryLocators.REMOVE_FROM_CART).click()
            wait_for(self).until(EC.invisibility_of_element_located((badge)))

    def go_to_cart(self):
        self.driver.find_element(*LoginPageLocators.CART_ICON).click()
