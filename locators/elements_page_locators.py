class TextBoxPageLocators:
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    # created area

    CREATED_FULL_NAME = ("xpath", "//p[@id='name']")
    CREATED_EMAIL = ("xpath", "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = ("xpath","//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    CHECKED_ITEMS = ("xpath", "//span/*[contains(@class, 'rct-icon-check')]")
    TITLE_ITEM = ".// ancestor::span[@class ='rct-text']"
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = ("xpath", "//label[@class = 'custom-control-label' and @for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = ("xpath", "//label[@class = 'custom-control-label' and @for='impressiveRadio']")
    NO_RADIOBUTTON = ("xpath", "//label[@class = 'custom-control-label' and @for='noRadio']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")

class WebTablePageLocators:
    ADD_BUTTON = ("xpath", "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = ("xpath", "//input[@id='firstName']")
    LASTNAME_INPUT = ("xpath", "//input[@id='lastName']")
    EMAIL_INPUT = ("xpath", "//input[@id='userEmail']")
    AGE_INPUT = ("xpath", "//input[@id='age']")
    SALARY_INPUT = ("xpath", "//input[@id='salary']")
    DEPARTMENT_INPUT = ("xpath", "//input[@id='department']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    # table
    PEOPLE_LIST = ("xpath", "//div[@class ='rt-tr-group']")
    SEARCH_INPUT = ("xpath", "//input[@id='searchBox']")
    DELETE_BUTTON = ("xpath", "//span[@title='Delete']")
    ROW_PARENT = ".// ancestor::div[@class ='rt-tr-group']"

    # update
    EDIT_BUTTON = ("xpath", "//span[@title='Edit']")
    NO_ROW_FOUND = ("xpath", "//div[contains(text(),'No rows found')]")

    ROW_PER_PAGE = ("xpath", "//select[@aria-label='rows per page']")

class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = ("xpath", "//button[text() ='Click Me']")
    DOUBLE_CLICK_MESSAGE = ("xpath", "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = ("xpath", "//p[@id='rightClickMessage']")
    CLICK_ME_MESSAGE = ("xpath", "//p[@id='dynamicClickMessage']")

class LinksPageLocators:
    SIMPLE_LINK = ("xpath", "(//a[@id='simpleLink'])")
    BAD_REQUEST = ("xpath", "(//a[@id='bad-request'])")

class UploadAndDownloadLocators:
    UPLOAD_FILE = ("xpath", "//input[@id='uploadFile']")
    UPLOADED_FILE_PATH = ("xpath", "//p[@id='uploadedFilePath']")
