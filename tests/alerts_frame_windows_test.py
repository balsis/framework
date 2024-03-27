import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertPage


class TestBrowserWindow:
    def test_new_tab(self, driver):
        new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_tab_page.open()
        result_text = new_tab_page.check_opened_tab()
        assert result_text == "This is a sample page"

    def test_new_window(self, driver):
        new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_window_page.open()
        result_text = new_window_page.check_opened_tab()
        assert result_text == "This is a sample page"


class TestAlertsPage:
    def test_see_alert(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == "You clicked a button"

    def test_alert_appear_5_sec(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()
        assert alert_text == "This alert appeared after 5 seconds"

    def test_confirm_alert(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()
        assert alert_text == "You selected Ok"
    def test_prompt_alert(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_text = alert_page.check_prompt_alert()
        assert alert_text == "You entered test"