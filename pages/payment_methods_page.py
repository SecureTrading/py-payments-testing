import time

import ioc_config
from configuration import CONFIGURATION
from locators.payment_methods_locators import PaymentMethodsLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
from utils.enums.payment_type import PaymentType
import json

from utils.helpers.request_executor import add_to_shared_dict, get_number_of_requests_with_data, \
    get_number_of_wallet_verify_requests, get_number_of_thirdparty_requests, get_number_of_requests_without_data, \
    get_number_of_requests_with_fraudcontroltransactionid_flag, \
    get_number_of_requests_with_data_and_fraudcontroltransactionid_flag, get_number_of_requests_with_updated_jwt, get_number_of_requests


class PaymentMethodsPage(BasePage):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def fill_credit_card_field(self, field_type, value):
        if field_type == FieldType.CARD_NUMBER.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.CARD_NUMBER.value,
                                                        PaymentMethodsLocators.card_number_input_field, value)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.EXPIRATION_DATE.value,
                                                        PaymentMethodsLocators.expiration_date_input_field, value)
        elif field_type == FieldType.SECURITY_CODE.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.SECURITY_CODE.value,
                                                        PaymentMethodsLocators.security_code_input_field, value)

    def fill_credit_card_field_ie_browser(self, field_type, value):
        if field_type == FieldType.CARD_NUMBER.name:
            self._action.switch_to_iframe_and_send_keys_one_by_one(FieldType.CARD_NUMBER.value,
                                                                   PaymentMethodsLocators.card_number_input_field,
                                                                   value)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            self._action.switch_to_iframe_and_send_keys_one_by_one(FieldType.EXPIRATION_DATE.value,
                                                                   PaymentMethodsLocators.expiration_date_input_field,
                                                                   value)
        elif field_type == FieldType.SECURITY_CODE.name:
            self._action.switch_to_iframe_and_send_keys_one_by_one(FieldType.SECURITY_CODE.value,
                                                                   PaymentMethodsLocators.security_code_input_field,
                                                                   value)

    def fill_payment_form(self, card_number, expiration_date, cvv):
        if "ie" in ioc_config.CONFIG.resolve('driver').browser:
            self.fill_credit_card_field_ie_browser(FieldType.CARD_NUMBER.name, card_number)
            self.fill_credit_card_field_ie_browser(FieldType.EXPIRATION_DATE.name, expiration_date)
            self.fill_credit_card_field_ie_browser(FieldType.SECURITY_CODE.name, cvv)
        else:
            self.fill_credit_card_field(FieldType.CARD_NUMBER.name, card_number)
            self.fill_credit_card_field(FieldType.EXPIRATION_DATE.name, expiration_date)
            self.fill_credit_card_field(FieldType.SECURITY_CODE.name, cvv)

    def fill_payment_form_without_cvv(self, card_number, expiration_date):
        if "ie" in ioc_config.CONFIG.resolve('driver').browser:
            self.fill_credit_card_field_ie_browser(FieldType.CARD_NUMBER.name, card_number)
            self.fill_credit_card_field_ie_browser(FieldType.EXPIRATION_DATE.name, expiration_date)
        else:
            self.fill_credit_card_field(FieldType.CARD_NUMBER.name, card_number)
            self.fill_credit_card_field(FieldType.EXPIRATION_DATE.name, expiration_date)

    def fill_merchant_input_field(self, field_type, value):
        if field_type == FieldType.NAME.name:
            self._action.send_keys(PaymentMethodsLocators.merchant_name, value)
        elif field_type == FieldType.EMAIL.name:
            self._action.send_keys(PaymentMethodsLocators.merchant_email, value)
        elif field_type == FieldType.PHONE.name:
            self._action.send_keys(PaymentMethodsLocators.merchant_phone, value)

    def fill_merchant_form(self, name, email, phone):
        self.fill_merchant_input_field(FieldType.NAME.name, name)
        self.fill_merchant_input_field(FieldType.EMAIL.name, email)
        self.fill_merchant_input_field(FieldType.PHONE.name, phone)

    def fill_amount_field(self, value):
        self._action.send_keys(PaymentMethodsLocators.amount_field, value)

    def get_payment_status_message(self):
        status_message = self._action.get_text_with_wait(PaymentMethodsLocators.notification_frame)
        return status_message

    def get_color_of_notification_frame(self):
        frame_color = self._action.get_element_attribute(PaymentMethodsLocators.notification_frame,
                                                         "data-notification-color")
        return frame_color

    def is_field_enabled(self, field_type):
        is_enabled = False
        if field_type == FieldType.CARD_NUMBER.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.CARD_NUMBER.value,
                                                                                    PaymentMethodsLocators.card_number_input_field)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.EXPIRATION_DATE.value,
                                                                                    PaymentMethodsLocators.expiration_date_input_field)
        elif field_type == FieldType.SECURITY_CODE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.SECURITY_CODE.value,
                                                                                    PaymentMethodsLocators.security_code_input_field)
        elif field_type == FieldType.SUBMIT_BUTTON.name:
            is_enabled = self._action.is_element_enabled(PaymentMethodsLocators.pay_mock_button)
        return is_enabled

    def choose_payment_methods(self, payment_type):
        if payment_type == PaymentType.VISA_CHECKOUT.name:
            self._executor.wait_for_javascript()
            self.scroll_to_bottom()
            self._executor.wait_for_element_visibility(PaymentMethodsLocators.visa_checkout_mock_button)
            if 'Catalina' in CONFIGURATION.REMOTE_OS_VERSION:
                self._action.click_by_javascript(PaymentMethodsLocators.visa_checkout_mock_button)
            else:
                self._action.click(PaymentMethodsLocators.visa_checkout_mock_button)
        elif payment_type == PaymentType.APPLE_PAY.name:
            self._executor.wait_for_javascript()
            self.scroll_to_bottom()
            if 'Catalina' in CONFIGURATION.REMOTE_OS_VERSION:
                self._action.click_by_javascript(PaymentMethodsLocators.apple_pay_mock_button)
            else:
                self._action.click(PaymentMethodsLocators.apple_pay_mock_button)
        elif payment_type == PaymentType.CARDINAL_COMMERCE.name:
            if 'Catalina' in CONFIGURATION.REMOTE_OS_VERSION or 'High Sierra' in CONFIGURATION.REMOTE_OS_VERSION:
                self._executor.wait_for_javascript()
                self._action.click_by_javascript(PaymentMethodsLocators.pay_mock_button)
            else:
                self._action.click(PaymentMethodsLocators.pay_mock_button)
        self._executor.wait_for_javascript()

    def get_field_validation_message(self, field_type):
        validation_message = ""
        if field_type == FieldType.CARD_NUMBER.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.CARD_NUMBER.value,
                                                                            PaymentMethodsLocators.card_number_field_validation_message)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.EXPIRATION_DATE.value,
                                                                            PaymentMethodsLocators.expiration_date_field_validation_message)
        elif field_type == FieldType.SECURITY_CODE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.SECURITY_CODE.value,
                                                                            PaymentMethodsLocators.security_code_field_validation_message)
        return validation_message

    def get_element_attribute(self, field_type, attribute):
        attribute_value = ""
        if field_type == FieldType.CARD_NUMBER.name:
            attribute_value = self._action.switch_to_iframe_and_get_element_attribute(FieldType.CARD_NUMBER.value,
                                                                                      PaymentMethodsLocators.card_number_input_field,
                                                                                      attribute)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            attribute_value = self._action.switch_to_iframe_and_get_element_attribute(FieldType.EXPIRATION_DATE.value,
                                                                                      PaymentMethodsLocators.expiration_date_input_field,
                                                                                      attribute)
        elif field_type == FieldType.SECURITY_CODE.name:
            attribute_value = self._action.switch_to_iframe_and_get_element_attribute(FieldType.SECURITY_CODE.value,
                                                                                      PaymentMethodsLocators.security_code_input_field,
                                                                                      attribute)
        elif field_type == FieldType.EMAIL.name:
            attribute_value = self._action.get_element_attribute(FieldType.EMAIL.value,
                                                                 PaymentMethodsLocators.merchant_email, attribute)
        return attribute_value

    def get_field_css_style(self, field_type, property):
        background_color = ""
        if field_type == FieldType.CARD_NUMBER.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.CARD_NUMBER.value,
                                                                               PaymentMethodsLocators.card_number_input_field,
                                                                               property)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.EXPIRATION_DATE.value,
                                                                               PaymentMethodsLocators.expiration_date_input_field,
                                                                               property)
        elif field_type == FieldType.SECURITY_CODE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.SECURITY_CODE.value,
                                                                               PaymentMethodsLocators.security_code_input_field,
                                                                               property)
        elif field_type == FieldType.NOTIFICATION_FRAME.name:
            background_color = self._action.get_css_value_with_wait(PaymentMethodsLocators.notification_frame, property)
        return background_color

    def is_field_displayed(self, field_type):
        is_displayed = False
        if field_type == FieldType.CARD_ICON.name:
            self._action.switch_to_iframe(FieldType.CARD_NUMBER.value)
            if len(self._action.find_elements(PaymentMethodsLocators.card_icon_in_input_field)) > 0:
                is_displayed = True
        elif field_type == FieldType.NOTIFICATION_FRAME.name:
            if len(self._action.find_elements(PaymentMethodsLocators.notification_frame)) > 0:
                if self._action.get_text_with_wait(PaymentMethodsLocators.notification_frame) != '':
                    is_displayed = True
        else:
            is_displayed = self._action.is_iframe_displayed(FieldType[field_type].value)
        return is_displayed

    def get_card_type_icon_from_input_field(self):
        credit_card_icon = self._action.switch_to_iframe_and_get_element_attribute(FieldType.CARD_NUMBER.value,
                                                                                   PaymentMethodsLocators.card_icon_in_input_field,
                                                                                   'alt')
        credit_card_icon = credit_card_icon.upper()
        return credit_card_icon

    def get_element_translation(self, field_type, locator):
        element_translation = ""
        if field_type == FieldType.CARD_NUMBER.name:
            element_translation = self._action.switch_to_iframe_and_get_text(FieldType.CARD_NUMBER.value,
                                                                             locator)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            element_translation = self._action.switch_to_iframe_and_get_text(FieldType.EXPIRATION_DATE.value,
                                                                             locator)
        elif field_type == FieldType.SECURITY_CODE.name:
            element_translation = self._action.switch_to_iframe_and_get_text(FieldType.SECURITY_CODE.value,
                                                                             locator)
        elif field_type == FieldType.SUBMIT_BUTTON.name:
            element_translation = self._action.get_text(locator)
        return element_translation

    def switch_to_parent_iframe(self):
        self._action.switch_to_iframe(FieldType.PARENT_IFRAME.value)

    def validate_field_validation_message(self, field_type, expected_message):
        actual_message = self.get_field_validation_message(field_type)
        assertion_message = f'{FieldType[field_type].name} field validation message is not correct, ' \
                            f'should be: "{expected_message}" but is: "{actual_message}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_message in actual_message, assertion_message

    def validate_payment_status_message(self, expected_message):
        if CONFIGURATION.REMOTE_DEVICE is not None:
            self.scroll_to_top()
        actual_message = self.get_payment_status_message()
        if len(actual_message) == 0:
            time.sleep(2)
            actual_message = self.get_payment_status_message()
        assertion_message = f'Payment status is not correct, should be: "{expected_message}" but is: "{actual_message}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_message in actual_message, assertion_message

    def validate_notification_frame_color(self, color):
        actual_color = self.get_color_of_notification_frame()
        assertion_message = f'Notification frame color is not correct, should be: "{color}" but is: "{actual_color}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert color in actual_color, assertion_message

    def validate_if_field_is_highlighted(self, field_type):
        attribute_value = self.get_element_attribute(field_type, "class")
        assertion_message = f'{FieldType[field_type].name} field is not highlighted but should be'
        add_to_shared_dict("assertion_message", assertion_message)
        assert "error" in attribute_value, assertion_message

    def validate_if_field_is_disabled(self, field_type):
        is_enabled = self.is_field_enabled(field_type)
        assertion_message = f'{FieldType[field_type].name} field is not disabled but should be'
        add_to_shared_dict("assertion_message", assertion_message)
        assert is_enabled is False, assertion_message

    def validate_if_field_is_enabled(self, field_type):
        is_enabled = self.is_field_enabled(field_type)
        assertion_message = f'{FieldType[field_type].name} field is not enabled but should be'
        add_to_shared_dict("assertion_message", assertion_message)
        assert is_enabled is True, assertion_message

    def validate_if_field_is_not_displayed(self, field_type):
        is_displayed = self.is_field_displayed(field_type)
        assertion_message = f'{FieldType[field_type].name} field is displayed but should not be'
        add_to_shared_dict("assertion_message", assertion_message)
        assert is_displayed is False, assertion_message

    def validate_css_style(self, field_type, property, expected_style):
        actual_css_style = self.get_field_css_style(field_type, property)
        assertion_message = f'{FieldType[field_type].name} style is not correct, ' \
                            f'should be  "{expected_style}" but is "{actual_css_style}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_style in actual_css_style, assertion_message

    def validate_element_translation(self, field_type, element, language, key):
        actual_translation = self.get_element_translation(field_type, element)
        expected_translation = self.get_translation_from_json(language, key)
        assertion_message = f"{FieldType[field_type].name} element translation is not correct: " \
                            f" should be {expected_translation} but is {actual_translation}"
        add_to_shared_dict("assertion_message", assertion_message)
        assert actual_translation in expected_translation, assertion_message

    def validate_labels_translation(self, language):
        self.validate_element_translation(FieldType.CARD_NUMBER.name, PaymentMethodsLocators.card_number_label,
                                          language,
                                          "Card number")
        self.validate_element_translation(FieldType.EXPIRATION_DATE.name, PaymentMethodsLocators.expiration_date_label,
                                          language, "Expiration date")
        self.validate_element_translation(FieldType.SECURITY_CODE.name, PaymentMethodsLocators.security_code_label,
                                          language,
                                          "Security code")
        self.validate_element_translation(FieldType.SUBMIT_BUTTON.name, PaymentMethodsLocators.pay_button_label,
                                          language,
                                          "Pay")

    def validate_message_translation_under_field(self, field_type, language, key):
        if field_type == FieldType.CARD_NUMBER.name:
            self.validate_element_translation(FieldType.CARD_NUMBER.name,
                                              PaymentMethodsLocators.card_number_field_validation_message, language,
                                              key)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            self.validate_element_translation(FieldType.EXPIRATION_DATE.name,
                                              PaymentMethodsLocators.expiration_date_field_validation_message, language,
                                              key)
        elif field_type == FieldType.SECURITY_CODE.name:
            self.validate_element_translation(FieldType.SECURITY_CODE.name,
                                              PaymentMethodsLocators.security_code_field_validation_message, language,
                                              key)

    def validate_payment_status_translation(self, language, key):
        self.validate_element_translation(FieldType.NOTIFICATION_FRAME.name,
                                          PaymentMethodsLocators.notification_frame, language, key)

    def get_translation_from_json(self, language, key):
        with open(f'resources/languages/{language}.json', 'r') as f:
            translation = json.load(f)
        return translation[key]

    def validate_if_url_contains_info_about_payment(self, expected_url):
        self._executor.wait_for_javascript()
        actual_url = self._executor.get_page_url()
        if expected_url not in actual_url:
            time.sleep(2)
            actual_url = self._executor.get_page_url()
        assertion_message = f'Url is not correct, should be: "{expected_url}" but is: "{actual_url}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_url in actual_url, assertion_message

    def validate_form_status(self, field_type, form_status):
        if 'enabled' in form_status:
            self.validate_if_field_is_enabled(field_type)
        else:
            self.validate_if_field_is_disabled(field_type)

    def validate_if_callback_popup_is_displayed(self, callback_popup):
        is_displayed = False
        if 'success' in callback_popup:
            is_displayed = self._action.is_element_displayed(PaymentMethodsLocators.callback_success_popup)
        elif 'error' in callback_popup:
            is_displayed = self._action.is_element_displayed(PaymentMethodsLocators.callback_error_popup)
        elif 'cancel' in callback_popup:
            is_displayed = self._action.is_element_displayed(PaymentMethodsLocators.callback_cancel_popup)
        assertion_message = f'{callback_popup} callback popup is not displayed but should be'
        add_to_shared_dict("assertion_message", assertion_message)
        assert is_displayed is True, assertion_message

    def validate_placeholders(self, card_number, exp_date, cvv):
        self.validate_placeholder(FieldType.CARD_NUMBER.name, card_number)
        self.validate_placeholder(FieldType.EXPIRATION_DATE.name, exp_date)
        self.validate_placeholder(FieldType.SECURITY_CODE.name, cvv)

    def validate_placeholder(self, field_type, expected_placeholder):
        actual_placeholder = self.get_element_attribute(field_type, "placeholder")
        assertion_message = f'Placeholder for {FieldType[field_type].name} field is not correct, should be {expected_placeholder}' \
                            f'but is {actual_placeholder}'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_placeholder in actual_placeholder, assertion_message

    def validate_credit_card_icon_in_input_field(self, expected_card_icon):
        actual_credit_card_icon = self.get_card_type_icon_from_input_field()
        assertion_message = f'Credit card icon is not correct, ' \
                            f'should be: "{expected_card_icon}" but is: "{actual_credit_card_icon}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_card_icon in actual_credit_card_icon, assertion_message

    def validate_number_of_requests_with_data(self, request_type, pan, expiry_date, cvv, expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests_with_data(request_type, pan, expiry_date, cvv)
        assertion_message = f'Number of {request_type} requests or request data are not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_requests_without_data(self, request_type, expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests_without_data(request_type)
        assertion_message = f'Number of {request_type} requests is not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_wallet_verify_requests(self, url, expected_number_of_requests):
        actual_number_of_requests = get_number_of_wallet_verify_requests(url)
        assertion_message = f'Number of {url} requests is not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_thirdparty_requests(self, request_type, walletsource, expected_number_of_requests):
        actual_number_of_requests = get_number_of_thirdparty_requests(request_type, walletsource)
        assertion_message = f'Number of request with {request_type} is not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_requests(self, request_type, pan, expiry_date, cvv, expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests(request_type, pan, expiry_date, cvv)
        assertion_message = f'Number of request with "{request_type}" is not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_requests_with_data_and_fraudcontroltransactionid_flag(self, request_type, pan, expiry_date,
                                                                                 cvv, expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type,
                                                                                                        pan,
                                                                                                        expiry_date,
                                                                                                        cvv)
        assertion_message = f'Number of {request_type} requests or request data are not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_number_of_requests_with_fraudcontroltransactionid_flag(self, request_type,
                                                                        expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests_with_fraudcontroltransactionid_flag(request_type)
        assertion_message = f'Number of {request_type} requests or request data are not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message

    def validate_updated_jwt_in_request(self, request_type, expected_number_of_requests):
        actual_number_of_requests = get_number_of_requests_with_updated_jwt(request_type)
        assertion_message = f'Number of {request_type} with updated jwt is not correct, ' \
                            f'should be: "{expected_number_of_requests}" but is: "{actual_number_of_requests}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_number_of_requests == actual_number_of_requests, assertion_message
