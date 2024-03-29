from locators.widgets_locators import AccordianPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException



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
