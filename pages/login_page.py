import time
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

    def login_with_timer(self, username, password):
        """Logs in and returns the time taken to load the inventory page."""
        self.load()
        start_time = time.time()
        self.login(username, password)

        wait_for(self.driver).until(
            EC.visibility_of_element_located((LoginPageLocators.INVENTORY_LIST))
        )

        load_time = time.time() - start_time
        return load_time
