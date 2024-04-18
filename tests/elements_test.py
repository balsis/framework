import os
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "the data doesn't match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Checkboxes have not been selected"

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_the_radio_button("no")
            # output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not be selected"
            assert output_impressive == 'Impressive', "'Impressive' have not be selected"
        # assert output_no == 'No', "'No' have not be selected. It's bug"

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.title('Сheck to add a person to the table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            result = web_table_page.check_added_person()
            assert new_person in result

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            # print(key_word)
            # print(table_result)
            assert key_word in table_result

        @allure.title('Checking to update the persons info in the table')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()  #
            row = web_table_page.check_search_person()
            assert age in row

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows in the table')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    @allure.feature('Buttons page')
    class TestButtonPage:

        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

    @allure.feature('Links page')
    class TestLinksPage:

        @allure.title('Checking the link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url

        @allure.title('Checking the broken link')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            responce_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert responce_code == 400

    @allure.feature('Upload and Download page')
    class TestUploadAndDownload:

        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_and_download_page.open()
            file_name, result = upload_and_download_page.upload_file()
            assert file_name == result

        @allure.title('Check download file')
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_and_download_page.open()
            check = upload_and_download_page.download_file()
            assert check is True

    @allure.feature('Dynamic properties page')
    class TestDynamicProperties:

        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != color_after

        @allure.title('Check appear button')
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True

        @allure.title('Check enable button')
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True
