from locators.payment_methods_locators import PaymentMethodsLocators
from pages.base_page import BasePage
from utils.enums.field_type import Field_type
from utils.enums.payment_type import Payment_type


class PaymentMethodsPage(BasePage, PaymentMethodsLocators):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def fill_credit_card__field(self, field_type, value):
        if field_type == Field_type.CARD_NUMBER.name:
            self._action.switch_to_iframe_and_send_keys(Field_type.CARD_NUMBER.value,
                                                        self._locators.card_number_input_field, value)
        elif field_type == Field_type.EXPIRATION_DATE.name:
            self._action.switch_to_iframe_and_send_keys(Field_type.EXPIRATION_DATE.value,
                                                        self._locators.expiration_date_input_field, value)
        elif field_type == Field_type.SECURITY_CODE.name:
            self._action.switch_to_iframe_and_send_keys(Field_type.SECURITY_CODE.value,
                                                        self._locators.security_code_input_field, value)

    def fill_payment_form(self, card_number, expiration_date, cvv):
        self.fill_credit_card__field(Field_type.CARD_NUMBER.name, card_number)
        self.fill_credit_card__field(Field_type.EXPIRATION_DATE.name, expiration_date)
        self.fill_credit_card__field(Field_type.SECURITY_CODE.name, cvv)

    def fill_merchant_input__field(self, field_type, value):
        if field_type == Field_type.NAME.name:
            self._action.send_keys(self._locators.merchant_name, value)
        elif field_type == Field_type.EMAIL.name:
            self._action.send_keys(self._locators.merchant_email, value)
        elif field_type == Field_type.PHONE.name:
            self._action.send_keys(self._locators.merchant_phone, value)

    def fill_merchant_form(self, name, email, phone):
        self.fill_merchant_input__field(Field_type.NAME.name, name)
        self.fill_merchant_input__field(Field_type.EMAIL.name, email)
        self.fill_merchant_input__field(Field_type.PHONE.name, phone)

    def get_payment_status_message(self):
        status_message = self._action.switch_to_iframe_and_get_text(Field_type.NOTIFICATION_FRAME.value,
                                                                    self._locators.notification_frame)
        return status_message

    def get_color_of_notification_frame(self):
        frame_color = self._action.switch_to_iframe_and_get_element_attribute(Field_type.NOTIFICATION_FRAME.value,
                                                                              self._locators.notification_frame,
                                                                              "data-notification-color")
        return frame_color

    def is_field_enabled(self, field_type):
        is_enabled = False
        if field_type == Field_type.CARD_NUMBER.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(Field_type.CARD_NUMBER.value,
                                                        self._locators.card_number_input_field)
        elif field_type == Field_type.EXPIRATION_DATE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(Field_type.EXPIRATION_DATE.value,
                                                        self._locators.expiration_date_input_field)
        elif field_type == Field_type.SECURITY_CODE.name:
            is_enabled = self._action.switch_to_iframe_and_check_is_element_enabled(Field_type.SECURITY_CODE.value,
                                                        self._locators.security_code_input_field)
        elif field_type == Field_type.SUBMIT_BUTTON.name:
            is_enabled = self._action.is_element_enabled(self._locators.pay_mock_button)
        return is_enabled

    def choose_payment_methods(self, payment_Type):
        if payment_Type == Payment_type.VISA_CHECKOUT.name:
            self._action.click(self._locators.visa_checkout_mock_button)
        elif payment_Type == Payment_type.APPLE_PAY.name:
            self._action.click(self._locators.apple_pay_mock_button)
        elif payment_Type == Payment_type.CARDINAL_COMMERCE.name:
            self._action.click(self._locators.pay_mock_button)

    def get_field_validation_message(self, field_type):
        validation_message = ""
        if field_type == Field_type.CARD_NUMBER.name:
            validation_message = self._action.switch_to_iframe_and_get_text(Field_type.CARD_NUMBER.value,
                                                                            self._locators.card_number_field_validation_message)
        elif field_type == Field_type.EXPIRATION_DATE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(Field_type.EXPIRATION_DATE.value,
                                                                            self._locators.expiration_date_field_validation_message)
        elif field_type == Field_type.SECURITY_CODE.name:
            validation_message = self._action.switch_to_iframe_and_get_text(Field_type.SECURITY_CODE.value,
                                                                            self._locators.security_code_field_validation_message)
        return validation_message

    def is_field_highlighted(self, field_type):
        is_highlighted = False
        class_name = ""
        if field_type == Field_type.CARD_NUMBER.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(Field_type.CARD_NUMBER.value,
                                                                                 self._locators.card_number_input_field,
                                                                                 "class")
        elif field_type == Field_type.EXPIRATION_DATE.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(Field_type.EXPIRATION_DATE.value,
                                                                                 self._locators.expiration_date_input_field,
                                                                                 "class")
        elif field_type == Field_type.SECURITY_CODE.name:
            class_name = self._action.switch_to_iframe_and_get_element_attribute(Field_type.SECURITY_CODE.value,
                                                                                 self._locators.security_code_input_field,
                                                                                 "class")
        elif field_type == Field_type.EMAIL.name:
            class_name = self._action.get_element_attribute(Field_type.EMAIL.value,
                                                            self._locators.merchant_email,
                                                            "class")
        if class_name.__contains__("error"):
            is_highlighted = True
        return is_highlighted

    def get_field_css_style(self, field_type, property):
        background_color = ""
        if field_type == Field_type.CARD_NUMBER.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(Field_type.CARD_NUMBER.value,
                                                                                 self._locators.card_number_input_field, property)
        elif field_type == Field_type.EXPIRATION_DATE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(Field_type.EXPIRATION_DATE.value,
                                                                                 self._locators.expiration_date_input_field, property)
        elif field_type == Field_type.SECURITY_CODE.name:
            background_color = self._action.switch_to_iframe_and_get_css_value(Field_type.SECURITY_CODE.value,
                                                                                 self._locators.security_code_input_field, property)
        return background_color

    def validate_field_validation_message(self, field_type, expected_message):
        actual_message = self.get_field_validation_message(field_type)
        assert expected_message in actual_message, f'Found "{actual_message}" instead'

    def validate_payment_status_message(self, expected_message):
        actual_message = self.get_payment_status_message()
        assert expected_message in actual_message, f'Found "{actual_message}" instead'

    def validate_notification_frame_color(self, color):
        actual_color = self.get_payment_status_message()
        assert color in actual_color, f'Found "{actual_color}" instead'

    def validate_if_field_is_highlighted(self, field_type):
        is_highlighted = self.is_field_highlighted(field_type)
        assert is_highlighted in True, 'Field is not highlighted'

    def validate_if_field_is_disabled(self, field_type):
        is_enabled= self.is_field_enabled(field_type)
        assert is_enabled in False, 'Field is not disabled'

    def validate_css_style(self, field_type, property, expected_style):
        actual_css_style= self.get_field_css_style(field_type)
        assert actual_css_style in expected_style, f'Found "{actual_css_style}" instead'




