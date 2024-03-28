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


class FramePageLocators:
    FRAME_1 = ("xpath", "//iframe[@id='frame1']")
    FRAME_2 = ("xpath", "//iframe[@id='frame2']")
    SAMPLE_HEADING = ("xpath", "//h1[@id='sampleHeading']")

class NestedFramePageLocators:
    PARENT_FRAME = ("xpath", "//iframe[@id='frame1']")
    CHILD_FRAME = ("xpath", "//body/iframe")

    PARENT_FRAME_TEXT = ("xpath", "//body[contains(text(),'Parent frame')]")
    CHILD_FRAME_TEXT = ("xpath", "//p[contains(text(),'Child Iframe')]")

class ModalDialogsPageLocators:
    SMALL_NODAL = ("xpath", "//button[@id='showSmallModal']")
    CLOSE_SMALL_BUTTON = ("xpath", "//button[@id='closeSmallModal']")
    SMALL_MODAL_TITLE = ("xpath", "//div[@class='modal-title h4']")
    SMALL_MODAL_BODY = ("xpath", "//div[@class='modal-body']")

    LARGE_MODAL = ("xpath", "//button[@id='showLargeModal']")
    CLOSE_LARGE_BUTTON = ("xpath", "//button[@id='closeLargeModal']")
    LARGE_MODAL_TITLE = ("xpath", "//div[@class='modal-title h4']")
    LARGE_MODAL_BODY = ("xpath", "//div[@class='modal-body']/p")