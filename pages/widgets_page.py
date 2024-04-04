import time
import random

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': {'title': self.locators.SECTION_1_HEADER,
                               'content': self.locators.SECTION_1_CONTENT},
                     'second': {'title': self.locators.SECTION_2_HEADER,
                                'content': self.locators.SECTION_2_CONTENT},
                     'third': {'title': self.locators.SECTION_3_HEADER,
                               'content': self.locators.SECTION_3_CONTENT}
                     }
        section_title = self.element_is_visible((accordian[accordian_num]['title']))
        section_title.click()
        try:
            section_content = self.element_is_visible((accordian[accordian_num]['content'])).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible((accordian[accordian_num]['content'])).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.elements_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.elements_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return [value_date_before, value_date_after]

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT, 10)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH, 10).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR, 10).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, "2020")
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT, 10)
        value_date_after = input_date_after.get_attribute("value")
        return [value_date_before, value_date_after]

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
