import os
import time

from locators.visa_checkout_locators import VisaCheckoutLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
from utils.helpers import gmail_service

from utils.enums.visa_checkout_field import VisaCheckoutField
from utils.helpers.gmail_service import EMAIL_LOGIN


class VisaCheckoutPage(BasePage, VisaCheckoutLocators):

    def click_visa_checkout_button(self):
        self._action.click(VisaCheckoutLocators.visa_checkout_button)

    def click_visa_checkout_close_button(self):
        self._waits.wait_until_iframe_is_presented_and_switch_to_it(FieldType.VISA_CHECKOUT.value)
        self._executor.wait_for_element_to_be_clickable(VisaCheckoutLocators.visa_close_popup_button)
        self._action.click(VisaCheckoutLocators.visa_close_popup_button)
        self._action.switch_to_parent_iframe()

    def fill_selected_field(self, field):
        if field == VisaCheckoutField.EMAIL_ADDRESS.value:
            self.fill_email_address(EMAIL_LOGIN)
        elif field == VisaCheckoutField.ONE_TIME_PASSWORD.value:
            self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_one_time_code)
            mail_ids = gmail_service.get_unseen_mail_ids_with_wait(8)
            self.fill_one_time_password_with_wait(mail_ids)
            if self._action.is_element_displayed(VisaCheckoutLocators.visa_one_time_code):
                mail_ids = gmail_service.get_last_five_mail_ids_with_wait(3)
                self.fill_one_time_password_with_wait(mail_ids)


    def fill_one_time_password_with_wait(self, mail_ids):
        mail_index = len(mail_ids)
        while mail_index and self._action.is_element_displayed(VisaCheckoutLocators.visa_one_time_code):
            code = gmail_service.get_verification_code_from_email_subject(mail_ids[mail_index - 1])
            self.fill_one_time_code(code)
            self.click_continue_checkout_process()
            mail_index -= 1
            time.sleep(4)


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

    def select_card_by_ending_number(self, card_number):
        self.visa_card_with_ending_number = card_number
        self._executor.wait_for_element_visibility(self.visa_card_with_ending_number)
        self._action.click(self.visa_card_with_ending_number)

    def fill_security_code(self):
        self._executor.wait_for_element_visibility(VisaCheckoutLocators.visa_security_code)
        self._action.send_keys(VisaCheckoutLocators.visa_security_code, '123')

    def is_security_code_displayed(self):
        if self._action.is_element_displayed(VisaCheckoutLocators.visa_security_code) is True:
            self.fill_security_code()
            self.click_continue_visa_payment_process()