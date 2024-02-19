class TextBoxPageLocators:
    # fields
    FULL_NAME = ('xpath', "//input[@id='userName']")
    EMAIL = ('xpath', "//input[@id='userEmail']")
    CURRENT_ADDRESS = ('xpath', "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ('xpath', "//textarea[@id='permanentAddress']")
    SUBMIT = ('xpath', "//button[@id='submit']")

    # created area

    CREATED_FULL_NAME = ('xpath', "//p[@id='name']")
    CREATED_EMAIL = ('xpath', "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ('xpath', "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = "//p[@id='permanentAddress']"


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    CHECKED_ITEMS = ("xpath", "//span/*[contains(@class, 'rct-icon-check')]")
    TITLE_ITEM = ".// ancestor::span[@class ='rct-text']"
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")

class RadioButtonPageLocators:
    YES_RADIOBUTTON = ("xpath", "//div[contains(@class, 'custom-control')]/input[@id='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = ("xpath", "//input[@id='impressiveRadio']")
    NO_RADIOBUTTON = ("xpath", "//input[@id='noRadio']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")


