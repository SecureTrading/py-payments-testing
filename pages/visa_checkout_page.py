from locators.visa_checkout_locators import VisaCheckoutLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
from utils.helpers import gmail_service

from utils.enums.visa_checkout_field import VisaCheckoutField


class VisaCheckoutPage(BasePage):

    def click_visa_checkout_button(self):
        self._action.click(VisaCheckoutLocators.visa_checkout_button)

    def fill_selected_field(self, field):
        if field == VisaCheckoutField.EMAIL_ADDRESS.value:
            self.fill_email_address("securetestpgs@gmail.com")
        elif field == VisaCheckoutField.ONE_TIME_PASSWORD.value:
            mail_ids = gmail_service.get_mail_ids_with_wiat(5)
            while self._action.is_element_displayed(VisaCheckoutLocators.visa_one_time_code):
                for mail_id in reversed(mail_ids):
                    code = gmail_service.get_verification_code_from_email_subject(mail_id)
                    self.fill_one_time_code(code)
                    self.click_continue_checkout_process()


    def fill_email_address(self, email):
        self._waits.wait_until_iframe_is_presented_and_switch_to_it(FieldType.VISA_CHECKOUT.value)
        self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_returning)
        self._action.click(VisaCheckoutLocators.visa_returning)
        self._action.send_keys(VisaCheckoutLocators.visa_email, email)

    def click_continue_checkout_process(self):
        self._executor.wait_for_element_to_be_clickable(VisaCheckoutLocators.visa_confirm_process)
        self._action.click(VisaCheckoutLocators.visa_confirm_process)

    def click_continue_visa_payment_process(self):
        self._executor.wait_for_element_to_be_clickable(VisaCheckoutLocators.visa_continue_payment_process)
        self._action.click(VisaCheckoutLocators.visa_continue_payment_process)

    def fill_one_time_code(self, one_time_code):
        self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_one_time_code)
        while self._action.get_element_attribute(VisaCheckoutLocators.visa_one_time_code, 'value') != '':
            self._action.delete_on_input(VisaCheckoutLocators.visa_one_time_code)
        self._action.send_keys(VisaCheckoutLocators.visa_one_time_code, one_time_code)