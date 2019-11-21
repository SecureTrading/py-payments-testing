import requests
from behave import *

from utils.mock_handler import stub_sample_json

use_step_matcher("re")

@then('the title should contain "(?P<title>.+)"')
def step_impl(context, title):
    sample_page = context.page_factory.get_page(page_name='sample')
    browser_title = sample_page.get_page_title()
    assert title in browser_title, f'Found "{browser_title}" instead'


@step("mock json should be visible on specific url")
def step_impl(context):
    stub_sample_json()
    response = requests.get('http://merchant.example.com:8084/test')
    print(response.content)
    assert response.content is not None