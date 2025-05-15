import pytest_check as check
from utils.wait_utils import wait_for
from utils.locators import CartPageLocators
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

    def verify_checkout_button_visual_position(self):
        wait_for(self.driver).until(
            EC.presence_of_element_located((CartPageLocators.CHECKOUT_BUTTON))
        )
        checkout_btn = self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)

        check.is_in(
            checkout_btn.value_of_css_property("position"),
            ["static", ""],
            "Unexpected 'position' CSS on checkout button",
        )
        check.is_in(
            checkout_btn.value_of_css_property("top"),
            ["auto", ""],
            "Unexpected 'top' CSS on checkout button",
        )
        check.is_in(
            checkout_btn.value_of_css_property("right"),
            ["auto", ""],
            "Unexpected 'right' CSS on checkout button",
        )
