import pytest
import pytest_html
import os
import base64
from selenium import webdriver

os.makedirs("screenshots", exist_ok=True)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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
            driver= item.funcargs.get("driver", None)
            if driver:
                ss_path = os.path.join(os.getcwd(), "screenshots", f"{item.name}.png")
                driver.save_screenshot(ss_path)

                with open(ss_path, "rb") as f:
                    encoded_image = base64.b64encode(f.read()).decode()
                html_image = f'<div><img src="data:image/png;base64,{encoded_image}" alt="Screenshot" style="width: 300px;"/></div>'
                extras.append(pytest_html.extras.html(html_image))
                extras.append(pytest_html.extras.url(driver.current_url))
        report.extras = extras