import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class Test_Elements:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        input_data = text_box_page.fill_all_fields()
        output_data = text_box_page.check_filled_form()
        assert input_data == output_data, "the data doesn't match"


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_result, "Checkboxes have not been selected"
class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/webtables")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        #radio_button_page.click_on_the_radio_button("no")
        #output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "'Yes' have not be selected"
        assert output_impressive == 'Impressive', "'Impressive' have not be selected"
       # assert output_no == 'No', "'No' have not be selected. It's bug"

class TestWebTable:
    def test_web_table_add_person(self,driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/radio-button")
        web_table_page.open()
