from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ReactJsAppLocators:

    home_tab: By = (By.ID, 'home')
    payment_details_tab: By = (By.ID, 'payment-details')
    personal_data_tab: By = (By.ID, 'personal-data')
    contact_data_tab: By = (By.ID, 'contact-data')
    payment_tab: By = (By.ID, 'payment')

    #personal_data_tab
    personal_data_title: By = (By.ID, 'st-form-title')