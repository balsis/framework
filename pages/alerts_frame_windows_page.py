import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertPageLocators, FramePageLocators, \
    NestedFramePageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_tab(self):
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_window(self):
        self.element_is_visible(self.locators.WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertPage(BasePage):
    locators = AlertPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys("test")
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_result


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame):
        if frame == "frame1":
            frame = self.element_is_present(self.locators.FRAME_1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.SAMPLE_HEADING).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame == "frame2":
            frame = self.element_is_present(self.locators.FRAME_2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.SAMPLE_HEADING).text
            self.driver.switch_to.default_content()
            return [text, width, height]

class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_NODAL).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        body_small = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.CLOSE_SMALL_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        body_large = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.CLOSE_LARGE_BUTTON).click()
        return [title_small, len(body_small)], [title_large, (len(body_large))]


