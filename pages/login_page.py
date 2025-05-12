from utils.locators import LoginPageLocators


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
