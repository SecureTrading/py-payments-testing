from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class VisaCheckoutLocators:

    def __init__(self):
        self._visa_card_with_ending_number = None

    # visa checkout fields
    visa_checkout_button: By = (By.ID, 'v-button')
    visa_content: By = (By.CLASS_NAME, 'content')
    visa_returning: By = (By.ID, 'tabs__tab-id__1')
    visa_email: By = (By.ID, 'email')
    visa_confirm_process: By = (By.CSS_SELECTOR, '.single-input-form .primary-button')
    visa_continue_payment_process: By = (By.NAME, 'btnContinue')
    visa_one_time_code: By = (By.CSS_SELECTOR, '.single-input-form #code')
    visa_close_popup_button: By = (By.CSS_SELECTOR, 'button.close:not(.icon)')
    visa_security_code: By = (By.ID, 'code')

    @property
    def visa_card_with_ending_number(self):
        return self._visa_card_with_ending_number

    @visa_card_with_ending_number.setter
    def visa_card_with_ending_number(self, ending_number):
        self._visa_card_with_ending_number = \
            (By.CSS_SELECTOR, f"button[aria-label*='{ending_number}']")