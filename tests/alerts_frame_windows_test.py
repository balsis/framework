import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertPage, FramePage, NestedFramePage, ModalDialogsPage
import allure
@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindow:
        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            result_text = new_tab_page.check_opened_tab()
            assert result_text == "This is a sample page"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            result_text = new_window_page.check_opened_tab()
            assert result_text == "This is a sample page"


    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button"

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds"

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok"
        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_prompt_alert()
            assert alert_text == "You entered test"

    @allure.feature('Frame Page')
    class TestFramesPage:
        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result1 = frame_page.check_frame('frame1')
            result2 = frame_page.check_frame('frame2')
            assert result1 == ['This is a sample page', '500px', '350px']
            assert result2 == ['This is a sample page', '100px', '100px']

    @allure.feature('Nested Page')
    class TestNestedFrames:
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame"
            assert child_text == "Child Iframe"

    @allure.feature('Modal Dialog Page')
    class TestModalDialogs:
        @allure.title('Check the page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] == 47
            assert large[1] == 574
