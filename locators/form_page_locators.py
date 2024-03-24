import random


class FormPageLocators:
    FIRST_NAME = ("xpath", "//input[@id='firstName']")
    LAST_NAME = ("xpath", "//input[@id='lastName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    MOBILE = ("xpath", "//input[@id='userNumber']")
    GENDER = ("xpath", f"//div[contains(@class, 'custom-radio')]/input[@id='gender-radio-{random.randint(1, 3)}']")
    DATE_OF_BIRTH = ("xpath", "//input[@id='dateOfBirthInput']")
    SUBJECT = ("xpath", "//input[@id='subjectsInput']")
    HOBBIES = ("xpath", f"//div[contains(@class, 'custom-checkbox')]/input[@id='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = ("xpath", "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = ("xpath", "textarea[id='currentAddress']")
    SELECT_STATE = ("xpath", "//div[@id='state']")
    STATE_INPUT = ("xpath", "//input[@id='react-select-3-input']")
    SELECT_CITY = ("xpath", "//div[@id='city']")
    CITY_INPUT = ("xpath", "//input[@id='react-select-4-input']")
    SUBMIT = ("xpath", "//button[@id='submit']")
