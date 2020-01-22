from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class AnimatedCardLocators:
    # animated card data
    animated_card: By = (By.ID, 'st-animated-card')
    credit_card_number_on_animated_card: By = (By.ID, 'st-animated-card-number')
    cvv_on_back_side_animated_card: By = (By.ID, 'st-animated-card-security-code')
    cvv_on_front_side_animated_card: By = (By.ID, 'st-animated-card-security-code-front-field')
    expiration_date_on_animated_card: By = (By.ID, 'st-animated-card-expiration-date')
    card_type_logo_from_animated_card: By = (By.ID, 'st-payment-logo')

    # labels
    card_number_label: By = (By.ID, 'st-animated-card-card-number-label')
    expiration_date_label: By = (By.ID, 'st-animated-card-expiration-date-label')
    security_code_label: By = (By.ID, 'st-animated-card-security-code-label')

    # inputs without iframes
    card_number_input_field: By = (By.ID, 'st-card-number-input')
    security_code_input_field: By = (By.ID, 'st-security-code-input')
    expiration_date_input_field: By = (By.ID, 'st-expiration-date-input')

    # Fields validation messages
    card_number_field_validation_message: By = (By.ID, 'st-card-number-message')
    expiration_date_field_validation_message: By = (By.ID, 'st-expiration-date-message')
    security_code_field_validation_message: By = (By.ID, 'st-security-code-message')
