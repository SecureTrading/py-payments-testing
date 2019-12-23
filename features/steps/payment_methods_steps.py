import requests
from behave import *
import time

from utils.enums.field_type import Field_type
from utils.logger import _get_logger
from utils.mock_handler import stub_sample_json

use_step_matcher("re")

# ToDo

@then('the title should contain "(?P<title>.+)"')
def step_impl(context, title):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    browser_title = payment_page.get_page_title()
    time.sleep(1)

    payment_page.fill_payment_form("411111111111", "12/22", "123")
    # print(payment_page.get_payment_status_message())
    # print(payment_page.get_color_of_notification_frame())
    time.sleep(2)
    print(payment_page.get_field_validation_message(Field_type.CARD_NUMBER.name))
    print(payment_page.is_field_highlighted(Field_type.CARD_NUMBER.name))
    print(payment_page.get_field_css_style(Field_type.CARD_NUMBER.name, "background-color"))
    # payment_page.validate_field_validation_message(Field_type.CARD_NUMBER.name, "test")
    time.sleep(3)
    assert title in browser_title, f'Found "{browser_title}" instead'


@step("mock json should be visible on specific url")
def step_impl(context):
    stub_sample_json()
    response = requests.get('http://merchant.example.com:8084/test')
    logger = _get_logger()
    logger.info(response.content)
    assert response.content is not None


