import time
import pytest_check as check
from utils.wait_utils import wait_for
from utils.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def check_error_massage(self):
        try:
            error = wait_for(self.driver, timeout=3).until(
                EC.visibility_of_element_located((LoginPageLocators.ERROR_MESSAGE))
            )
            error_text = error.text
            return error.text.partition(":")[2].strip()
        except:
            return "No error message displayed"

    def check_login(self, username, password):
        """Logs in and returns the time taken to load the inventory page."""
        self.load()
        start_time = time.time()
        self.login(username, password)
        if "inventory" not in self.driver.current_url:
            error_msg = self.check_error_massage()
            check.is_in(
                "inventory", self.driver.current_url, f"Login Failed: {error_msg}"
            )
        else:
            check.is_in("inventory", self.driver.current_url)

            wait_for(self.driver).until(
                EC.visibility_of_element_located((LoginPageLocators.INVENTORY_LIST))
            )

            load_time = time.time() - start_time
            # return load_time
            check.less(
                load_time,
                2,
                f"Unexpected glitch delay, load time was {load_time:.2f} seconds",
            )
