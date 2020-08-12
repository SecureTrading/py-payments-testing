from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class VisaCheckoutLocators:
    # visa checkout fields
    visa_checkout_button: By = (By.ID, 'v-button')
    visa_content: By = (By.CLASS_NAME, 'content')
    visa_returning: By = (By.ID, 'tabs__tab-id__1')
    visa_email: By = (By.ID, 'email')
    visa_confirm_process: By = (By.CSS_SELECTOR, '.single-input-form .primary-button')
    visa_continue_payment_process: By = (By.NAME, 'btnContinue')
    visa_one_time_code: By = (By.CSS_SELECTOR, '.single-input-form #code')
