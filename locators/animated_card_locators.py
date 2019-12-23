from attrdict import AttrDict
from selenium.webdriver.common.by import By


class AnimatedCardLocators:
    _locators = AttrDict({
        # animated card data
        'animated_card': (By.ID, 'st-animated-card'),
        'credit_card_number_on_animated_card': (By.ID, 'st-animated-card-number'),
        'cvv_on_back_side_animated_card': (By.ID, 'st-animated-card-security-code'),
        'cvv_on_front_side_animated_card': (By.ID, 'st-animated-card-security-code-front-field'),
        'expiration_date_on_animated_card': (By.ID, 'st-animated-card-expiration-date'),
        'card_type_logo_from_animated_card': (By.ID, 'st-payment-log'),

        # labels
        'card_number_label': (By.ID, 'st-animated-card-card-number-label'),
        'expiration_date_label': (By.ID, 'st-animated-card-expiration-date-label'),
        'security_code_label': (By.ID, 'st-animated-card-security-code-label'),

        # inputs without iframes
        'card_number_input_field': (By.ID, 'st-card-number-input'),
        'cvv_input_field': (By.ID, 'st-security-code-input'),
        'expiration_date_input_field': (By.ID, 'st-expiration-date-input'),

    })
