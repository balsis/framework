class AccordianPageLocators:
    SECTION_1_HEADER = ("xpath", "//div[@id='section1Heading']")
    SECTION_1_CONTENT = ("xpath", "//div[@id='section1Content']/p")
    SECTION_2_HEADER = ("xpath", "//div[@id='section2Heading']")
    SECTION_2_CONTENT = ("xpath", "//div[@id='section2Content']/p")
    SECTION_3_HEADER = ("xpath", "//div[@id='section3Heading']")
    SECTION_3_CONTENT = ("xpath", "//div[@id='section3Content']/p")

class AutoCompletePageLocators:
    MULTI_INPUT = ("xpath", "//input[@id='autoCompleteMultipleInput']")
    MULTI_VALUE = ("xpath", "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_REMOVE = ("xpath", "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']//*[name()='svg']/*")
    MULTI_VALUE_REMOVE_ALT = ("css", "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    SINGLE_VALUE = ("xpath", "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = ("xpath", "//input[@id='autoCompleteSingleInput']")


