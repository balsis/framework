class BrowserWindowsPageLocators:
    TAB_BUTTON = ("xpath", "//button[@id='tabButton']")
    WINDOW_BUTTON = ("xpath", "//button[@id='windowButton']")

    TITLE_NEW = ("xpath", "//h1[@id='sampleHeading']")

class AlertPageLocators:
   ALERT_BUTTON = ("xpath", "//button[@id='alertButton']")
   TIMER_ALERT_AFTER_5_SEC_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
   CONFIRM_BOX_ALERT_BUTTON = ("xpath", "//button[@id='confirmButton']")
   PROMPT_BOX_ALERT_BUTTON = ("xpath", "//button[@id='promtButton']")
   CONFIRM_RESULT = ("xpath", "//span[@id='confirmResult']")
   PROMPT_RESULT = ("xpath", "//span[@id='promptResult']")