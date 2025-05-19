import os
import yaml
import base64
import pytest
import pytest_html
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    },
)
chrome_options.add_argument("--headless")


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "swaglabs_selenium_pytest"

    # Ensure the screenshots folder exists
    os.makedirs("screenshots", exist_ok=True)


def read_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def config():
    return read_config()


# --- Add CLI Option for browser ---
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome, firefox, edge",
    )

    parser.addoption(
        "--headed", action="store_true", default=False, help="Run tests in headed mode"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("browser").lower()
    # headed = request.config.getoption("headed")
    # if not headed:
    # chrome_options.add_orgument("--headless")
    if browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Unsupported browser")
    # driver.implicitly_wait(config["timeout"])
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("browser", None)
            if driver:
                ss_path = os.path.join(os.getcwd(), "screenshots", f"{item.name}.png")
                driver.save_screenshot(ss_path)

                with open(ss_path, "rb") as f:
                    encoded_image = base64.b64encode(f.read()).decode()

                html_image = f'<div><img src="data:image/png;base64,{encoded_image}" alt="Screenshot" style="width: 300px;"/></div>'
                extras.append(pytest_html.extras.html(html_image))

                extras.append(pytest_html.extras.url(driver.current_url))

        report.extras = extras
