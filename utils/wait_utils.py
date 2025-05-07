from selenium.webdriver.support.ui import WebDriverWait


def wait_for(driver, timeout=10):
    return WebDriverWait(driver, timeout)
