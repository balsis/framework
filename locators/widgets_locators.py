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
    MULTI_VALUE_REMOVE = (
        "xpath", "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']//*[name()='svg']/*")
    MULTI_VALUE_REMOVE_ALT = ("css", "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    SINGLE_VALUE = ("xpath", "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = ("xpath", "//input[@id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    DATE_INPUT = ("xpath", "//input[@id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = ("xpath", "//select[@class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = ("xpath", "//select[@class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = ("xpath", "//div[contains(@class, 'react-datepicker__day react-datepicker__day')]")

    DATE_AND_TIME_INPUT = ("xpath", "//input[@id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = ("xpath", "//div[@class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = ("xpath", "//div[@class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = ("xpath", "//li[@class='react-datepicker__time-list-item ']")

    DATE_AND_TIME_MONTH_LIST = ("xpath", "//div[contains(@class, 'react-datepicker__month-option')]")
    DATE_AND_TIME_YEAR_LIST = ("xpath", "//div[contains(@class, 'react-datepicker__year-option')]")


class SliderPageLocators:
    INPUT_SLIDER = ("xpath", "//input[@class='range-slider range-slider--primary']")
    SLIDER_VALUE = ("xpath", "//input[@id='sliderValue']")


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = ("xpath", "//button[@id='startStopButton']")
    PROGRESS_BAR_VALUE = ("xpath", "//div[@class='progress-bar bg-info']")
