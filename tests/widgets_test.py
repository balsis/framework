import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


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

class TestTabsPage:
    def test_tabs(self, driver):
        tabs = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs.open()
        what_button, what_content = tabs.check_tabs('what')
        origin_button, origin_content = tabs.check_tabs('origin')
        use_button, use_content = tabs.check_tabs('use')
        # more_button, more_content = tabs.check_tabs('more')
        assert what_button == 'What' and what_content != 0
        assert origin_button == 'Origin' and origin_content != 0
        assert use_button == 'Use' and use_content != 0
        # assert more_button == 'More' and what_content != 0

class TestToolTips:
    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        button_text, input_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
        assert input_text == 'You hovered over the text field', 'hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

class TestMenuPage:
    def test_menu_items(self, driver):
        menu_page = MenuPage(driver, 'https://demoqa.com/menu')
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                        'Sub Sub Item 2', 'Main Item 3'], "menu items do not exist or have not been selected"