import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestAccordianPage:
    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
        assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
        assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'


class TestAutoCompletePage:
    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result

    def test_remove_value_from_multi(self, driver):
        autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
        assert count_value_before != count_value_after

    def test_fill_single_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result


class TestDatePickerPage:
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_after != value_date_before

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_after != value_date_before

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            assert value_after != value_before

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progress_bar_value()
            assert value_before < value_after
