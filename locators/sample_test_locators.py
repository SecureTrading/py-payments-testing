from attrdict import AttrDict
from selenium.webdriver.common.by import By


class SamplePageLocators:
    _locators = AttrDict({
        'search_input': (By.XPATH, '//input[@name="q"]'),
    })