import ioc_config
from configuration import CONFIGURATION
from locators.visa_checkout_locators import VisaCheckoutLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
import json

from utils.enums.visa_checkout_field import VisaCheckoutField


class VisaCheckoutPage(BasePage):

    def click_visa_checkout_button(self):
        self._action.click(VisaCheckoutLocators.visa_checkout_button)

    def fill_selected_field(self, field):
        #ToDo - use email and one time password from gmail
        if field == VisaCheckoutField.EMAIL_ADDRESS.value:
            self.fill_email_address("test@test.pl")
        elif field == VisaCheckoutField.ONE_TIME_PASSWORD.value:
            self.fill_one_time_code("1234")

    def fill_email_address(self, email):
        self._waits.wait_until_iframe_is_presented_and_switch_to_it(FieldType.VISA_CHECKOUT.value)
        self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_returning)
        self._action.click(VisaCheckoutLocators.visa_returning)
        self._action.send_keys(VisaCheckoutLocators.visa_email, email)

    def click_continue_checkout_process(self):
        self._executor.wait_for_element_to_be_clickable(VisaCheckoutLocators.visa_confirm_process)
        self._action.click(VisaCheckoutLocators.visa_confirm_process)

    def fill_one_time_code(self, one_time_code):
        self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_one_time_code)
        self._action.send_keys(VisaCheckoutLocators.visa_one_time_code, one_time_code)