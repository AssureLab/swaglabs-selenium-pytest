from utils.wait_utils import wait_for
from utils.inventory_locators import InventoryLocators
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_and_remove_items(self):
        add_list = self.driver.find_elements(*InventoryLocators.ADD_TO_CART)
        for add in add_list:
            add.click()
            badge = self.driver.find_element(*InventoryLocators.BADGE)
            assert "1" == badge.text
            self.driver.find_element(*InventoryLocators.REMOVE_FROM_CART).click()
            wait_for(self).until(EC.invisibility_of_element_located((badge)))
