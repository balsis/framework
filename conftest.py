from datetime import datetime

import pytest
import allure
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    else:
        raise ValueError("Unsupported browser")

    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
