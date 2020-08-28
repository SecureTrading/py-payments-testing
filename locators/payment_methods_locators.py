from dataclasses import dataclass
from selenium.webdriver.common.by import By

from utils.enums.field_type import FieldType


@dataclass
class PaymentMethodsLocators:
    # merchant input fields
    merchant_name: By = (By.ID, 'st-form-last-name')
    merchant_email: By = (By.ID, 'st-form-email')
    merchant_phone: By = (By.ID, 'st-form-phone')
    amount_field: By = (By.ID, 'example-form-amount')

    # Credit card form
    secure_trade_form: By = (By.ID, "st-control-frame-iframe")
    card_number_input_field: By = (By.ID, 'st-card-number-input')
    expiration_date_input_field: By = (By.ID, 'st-expiration-date-input')
    security_code_input_field: By = (By.ID, 'st-security-code-input')

    # Fields validation messages
    card_number_field_validation_message: By = (By.ID, 'st-card-number-message')
    expiration_date_field_validation_message: By = (By.ID, 'st-expiration-date-message')
    security_code_field_validation_message: By = (By.ID, 'st-security-code-message')

    # Notification frame
    notification_frame: By = (By.CSS_SELECTOR, '.st-form__group.notification-frame')

    # Iframe
    card_number_iframe: By = (By.ID, FieldType.CARD_NUMBER.value)
    expiration_date_iframe: By = (By.ID, FieldType.EXPIRATION_DATE.value)
    security_code_iframe: By = (By.ID, FieldType.SECURITY_CODE.value)
    animated_card_iframe: By = (By.ID, FieldType.ANIMATED_CARD.value)
    parent_iframe: By = (By.ID, FieldType.PARENT_IFRAME.value)

    # payment methods
    pay_mock_button: By = (By.ID, 'merchant-submit-button')
    visa_checkout_mock_button: By = (By.ID, 'v-button')
    apple_pay_mock_button: By = (By.ID, 'st-apple-pay')

    # labels
    card_number_label: By = (By.XPATH, '//label[@for="st-card-number-input"]')
    expiration_date_label: By = (By.XPATH, '//label[@for="st-expiration-date-input"]')
    security_code_label: By = (By.XPATH, '//label[@for="st-security-code-input"]')
    pay_button_label: By = (By.XPATH, '//button[@type="submit"]')

    callback_success_popup: By = (By.ID, 'success-popup')
    callback_error_popup: By = (By.ID, 'error-popup')
    callback_cancel_popup: By = (By.ID, 'cancel-popup')
    callback_data_popup: By = (By.ID, 'data-popup')
    callback_success_counter: By = (By.ID, 'success-callback-counter')
    callback_error_counter: By = (By.ID, 'error-callback-counter')
    callback_cancel_counter: By = (By.ID, 'cancel-callback-counter')
    callback_submit_counter: By = (By.ID, 'submit-callback-counter')

    card_icon_in_input_field: By = (By.ID, 'card-icon')

    cardinal_v2_authentication_code_field: By = (By.CLASS_NAME, 'input-field')
    cardinal_v2_authentication_submit_btn: By = (By.CLASS_NAME, 'primary')
    additional_button: By = (By.ID, 'additional-button')

    cardinal_v1_authentication_code_field: By = (By.ID, 'password')
    cardinal_v1_authentication_submit_btn: By = (By.NAME, 'UsernamePasswordEntry')

    not_private_connection_text: By = (By.XPATH, "//*[contains(text(),'This Connection Is Not Private')]")