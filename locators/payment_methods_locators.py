from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class PaymentMethodsLocators:
    # merchant input fields
    merchant_name: By = (By.ID, 'example-form-name')
    merchant_email: By = (By.ID, 'example-form-email')
    merchant_phone: By = (By.ID, 'example-form-phone')
    amount_field: By = (By.ID, 'example-form-amount')

    # Credit card form
    card_number_input_field: By = (By.ID, 'st-card-number-input')
    expiration_date_input_field: By = (By.ID, 'st-expiration-date-input')
    security_code_input_field: By = (By.ID, 'st-security-code-input')

    # Fields validation messages
    card_number_field_validation_message: By = (By.ID, 'st-card-number-message')
    expiration_date_field_validation_message: By = (By.ID, 'st-expiration-date-message')
    security_code_field_validation_message: By = (By.ID, 'st-security-code-message')

    # Notification frame
    notification_frame: By = (By.ID, 'st-notification-frame')

    # payment methods
    pay_mock_button: By = (By.ID, 'merchant-submit-button')
    visa_checkout_mock_button: By = (By.ID, 'v-button')
    apple_pay_mock_button: By = (By.ID, 'st-apple-pay')

    # labels
    card_number_label: By = (By.XPATH, '//label[@for="st-card-number-input"]')
    expiration_date_label: By = (By.XPATH, '//label[@for="st-expiration-date-input"]')
    security_code_label: By = (By.XPATH, '//label[@for="st-security-code-input"]')
    pay_button_label: By = (By.XPATH, '//button[@type="submit"]')
