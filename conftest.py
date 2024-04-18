from datetime import datetime

import pytest
import allure
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome, firefox or safari")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.page_load_strategy = 'eager'
        options.add_argument("--headless")
        options.add_argument('--incognito')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-cache")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--headless")
        options.add_argument('--incognito')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-cache")
        driver = webdriver.Firefox(options=options)
    elif browser == "safari":
        options = webdriver.SafariOptions()
        options.page_load_strategy = 'eager'
        # options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--incognito')
        options.add_argument('--disable-gpu')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-cache")
        driver = webdriver.Safari(options=options)
    else:
        raise ValueError("Unsupported browser")

    yield driver
    # attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
