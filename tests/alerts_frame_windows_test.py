import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


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
