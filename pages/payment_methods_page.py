from locators.payment_methods_locators import PaymentMethodsLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
from utils.enums.payment_type import PaymentType
import json


class PaymentMethodsPage(BasePage, PaymentMethodsLocators):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def fill_credit_card_field(self, field_type, value):
        if field_type == FieldType.CARD_NUMBER.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.CARD_NUMBER.value,
                                                        self._locators.card_number_input_field, value)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.EXPIRATION_DATE.value,
                                                        self._locators.expiration_date_input_field, value)
        elif field_type == FieldType.SECURITY_CODE.name:
            self._action.switch_to_iframe_and_send_keys(FieldType.SECURITY_CODE.value,
                                                        self._locators.security_code_input_field, value)

    def fill_payment_form(self, card_number, expiration_date, cvv):
        self.fill_credit_card_field(FieldType.CARD_NUMBER.name, card_number)
        self.fill_credit_card_field(FieldType.EXPIRATION_DATE.name, expiration_date)
        self.fill_credit_card_field(FieldType.SECURITY_CODE.name, cvv)

    def fill_merchant_input_field(self, field_type, value):
        if field_type == FieldType.NAME.name:
            self._action.send_keys(self._locators.merchant_name, value)
        elif field_type == FieldType.EMAIL.name:
            self._action.send_keys(self._locators.merchant_email, value)
        elif field_type == FieldType.PHONE.name:
            self._action.send_keys(self._locators.merchant_phone, value)

    def fill_merchant_form(self, name, email, phone):
        self.fill_merchant_input_field(FieldType.NAME.name, name)
        self.fill_merchant_input_field(FieldType.EMAIL.name, email)
        self.fill_merchant_input_field(FieldType.PHONE.name, phone)

    def get_payment_status_message(self):
        status_message = self._action.switch_to_iframe_and_get_text(FieldType.NOTIFICATION_FRAME.value,
                                                                    self._locators.notification_frame)
        return status_message

    def get_color_of_notification_frame(self):
        frame_color = self._action.switch_to_iframe_and_get_element_attribute(FieldType.NOTIFICATION_FRAME.value,
                                                                              self._locators.notification_frame,
                                                                              "data-notification-color")
        return frame_color

    def is_field_enabled(self, field_type):
        is_enabled = False
        if field_type == FieldType.CARD_NUMBER.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.CARD_NUMBER.value,
                                                                                    self._locators.card_number_input_field)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.EXPIRATION_DATE.value,
                                                                                    self._locators.expiration_date_input_field)
        elif field_type == FieldType.SECURITY_CODE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(FieldType.SECURITY_CODE.value,
                                                                                    self._locators.security_code_input_field)
        elif field_type == FieldType.SUBMIT_BUTTON.name:
            is_enabled = self._action.is_element_enabled(self._locators.pay_mock_button)
        return is_enabled

    def choose_payment_methods(self, payment_type):
        if payment_type == PaymentType.VISA_CHECKOUT.name:
            self._action.click(self._locators.visa_checkout_mock_button)
        elif payment_type == PaymentType.APPLE_PAY.name:
            self._action.click(self._locators.apple_pay_mock_button)
        elif payment_type == PaymentType.CARDINAL_COMMERCE.name:
            self._action.click(self._locators.pay_mock_button)

    def get_field_validation_message(self, field_type):
        validation_message = ""
        if field_type == FieldType.CARD_NUMBER.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.CARD_NUMBER.value,
                                                                            self._locators.card_number_field_validation_message)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.EXPIRATION_DATE.value,
                                                                            self._locators.expiration_date_field_validation_message)
        elif field_type == FieldType.SECURITY_CODE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(FieldType.SECURITY_CODE.value,
                                                                            self._locators.security_code_field_validation_message)
        return validation_message

    def is_field_highlighted(self, field_type):
        is_highlighted = False
        class_name = ""
        if field_type == FieldType.CARD_NUMBER.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(FieldType.CARD_NUMBER.value,
                                                                                 self._locators.card_number_input_field,
                                                                                 "class")
        elif field_type == FieldType.EXPIRATION_DATE.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(FieldType.EXPIRATION_DATE.value,
                                                                                 self._locators.expiration_date_input_field,
                                                                                 "class")
        elif field_type == FieldType.SECURITY_CODE.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(FieldType.SECURITY_CODE.value,
                                                                                 self._locators.security_code_input_field,
                                                                                 "class")
        elif field_type == FieldType.EMAIL.name:
            class_name = self._action.get_element_attribute(FieldType.EMAIL.value,
                                                            self._locators.merchant_email,
                                                            "class")
        if class_name.__contains__("error"):
            is_highlighted = True
        return is_highlighted

    def get_field_css_style(self, field_type, property):
        background_color = ""
        if field_type == FieldType.CARD_NUMBER.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.CARD_NUMBER.value,
                                                                               self._locators.card_number_input_field,
                                                                               property)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.EXPIRATION_DATE.value,
                                                                               self._locators.expiration_date_input_field,
                                                                               property)
        elif field_type == FieldType.SECURITY_CODE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(FieldType.SECURITY_CODE.value,
                                                                               self._locators.security_code_input_field,
                                                                               property)
        return background_color

    def is_field_displayed(self, field_type):
        is_displayed = False
        if field_type == FieldType.CARD_NUMBER.name:
            is_displayed = self._action.is_element_displayed(self._locators.card_number_input_field)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            is_displayed = self._action.is_element_displayed(self._locators.expiration_date_input_field)
        elif field_type == FieldType.SECURITY_CODE.name:
            is_displayed = self._action.is_element_displayed(self._locators.security_code_input_field)
        elif field_type == FieldType.SUBMIT_BUTTON.name:
            is_displayed = self._action.is_element_displayed(self._locators.pay_mock_button)
        return is_displayed

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

    def validate_field_validation_message(self, field_type, expected_message):
        actual_message = self.get_field_validation_message(field_type)
        assert expected_message in actual_message, f'{FieldType[field_type].name} field validation message is not correct, ' \
                                                   f'should be: "{expected_message}" but is: "{actual_message}"'

    def validate_payment_status_message(self, expected_message):
        actual_message = self.get_payment_status_message()
        assert expected_message in actual_message, f'Payment status is not correct, ' \
                                                   f'should be: "{expected_message}" but is: "{actual_message}"'

    def validate_notification_frame_color(self, color):
        actual_color = self.get_payment_status_message()
        assert color in actual_color, f'Notification frame color is not correct, ' \
                                      f'should be: "{color}" but is: "{actual_color}"'

    def validate_if_field_is_highlighted(self, field_type):
        is_highlighted = self.is_field_highlighted(field_type)
        assert is_highlighted is True, f'{FieldType[field_type].name} field is not highlighted but should be'

    def validate_if_field_is_disabled(self, field_type):
        is_enabled = self.is_field_enabled(field_type)
        assert is_enabled is False, f'{FieldType[field_type].name} field is not disabled but should be'

    def validate_if_field_is_enabled(self, field_type):
        is_enabled = self.is_field_enabled(field_type)
        assert is_enabled is True, f'{FieldType[field_type].name} field is not enabled but should be'

    def validate_if_field_is_not_displayed(self, field_type):
        is_displayed = self.is_field_displayed(field_type)
        assert is_displayed is False, f'{FieldType[field_type].name} field is displayed but should not be'

    def validate_css_style(self, field_type, property, expected_style):
        actual_css_style = self.get_field_css_style(field_type, property)
        assert actual_css_style in expected_style, f'{FieldType[field_type].name} style is not correct, ' \
                                                   f'should be  "{expected_style}" but is "{expected_style}"'

    def validate_element_translation(self, field_type, element, language, key):
        actual_translation = self.get_element_translation(field_type, element)
        expected_translation = self.get_translation_from_json(language, key)
        assert actual_translation in expected_translation, f"{FieldType[field_type].name} element translation is not correct: " \
                                                           f" should be {expected_translation} but is {actual_translation}"

    def validate_labels_translation(self, language):
        self.validate_element_translation(FieldType.CARD_NUMBER.name, self._locators.card_number_label, language,
                                          "Card number")
        self.validate_element_translation(FieldType.EXPIRATION_DATE.name, self._locators.expiration_date_label,
                                          language, "Expiration date")
        self.validate_element_translation(FieldType.SECURITY_CODE.name, self._locators.security_code_label, language,
                                          "Security code")
        self.validate_element_translation(FieldType.SUBMIT_BUTTON.name, self._locators.pay_button_label, language,
                                          "Pay")

    def validate_message_translation_under_field(self, field_type, language, key):
        if field_type == FieldType.CARD_NUMBER.name:
            self.validate_element_translation(FieldType.CARD_NUMBER.name,
                                              self._locators.card_number_field_validation_message, language, key)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            self.validate_element_translation(FieldType.EXPIRATION_DATE.name,
                                              self._locators.expiration_date_field_validation_message, language, key)
        elif field_type == FieldType.SECURITY_CODE.name:
            self.validate_element_translation(FieldType.SECURITY_CODE.name,
                                              self._locators.security_code_field_validation_message, language, key)

    def validate_payment_status_translation(self, language, key):
        self.validate_element_translation(FieldType.NOTIFICATION_FRAME.name,
                                          self._locators.notification_frame, language, key)

    def get_translation_from_json(self, language, key):
        with open(f'resources/languages/{language}.json', 'r') as f:
            translation = json.load(f)
        return translation[key]

    def validate_if_url_contains_info_about_payment(self, expected_url):
        actual_url = self._executor.get_page_url()
        assert expected_url in actual_url, f'Url is not correct, ' \
                                           f'should be: "{expected_url}" but is: "{actual_url}"'
