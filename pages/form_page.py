from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = next(generated_file())
