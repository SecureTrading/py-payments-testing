from attrdict import AttrDict
from selenium.webdriver.common.by import By


class PaymentMethodsLocators:
    _locators = AttrDict({
        # merchant input fields
        'merchant_name': (By.ID, 'example-form-name'),
        'merchant_email': (By.ID, 'example-form-email'),
        'merchant_phone': (By.ID, 'example-form-phone'),

        # Credit card form
        'card_number_input_field': (By.ID, 'st-card-number-input'),
        'expiration_date_input_field': (By.ID, 'st-expiration-date-input'),
        'security_code_input_field': (By.ID, 'st-security-code-input'),

        # Fields validation messages
        'card_number_field_validation_message': (By.ID, 'st-card-number-message'),
        'expiration_date_field_validation_message': (By.ID, 'st-expiration-date-message'),
        'security_code_field_validation_message': (By.ID, 'st-security-code-message'),

        # Notification frame
        'notification_frame': (By.ID, 'st-notification-frame'),

        # payment methods
        'pay_mock_button': (By.ID, 'merchant-submit-button'),
        'visa_checkout_mock_button': (By.ID, 'v-button'),
        'apple_pay_mock_button': (By.ID, 'st-apple-pay'),

        # labels
        'card_number_label': (By.XPATH, '//label[@for="st-card-number-input'),
        'expiration_date_label': (By.XPATH, '//label[@for="st-expiration-date-input'),
        'security_code_label': (By.XPATH, '//label[@for="st-security-code-input'),
        'pay_button_label': (By.XPATH, '//button[@type="submit'),
    })
