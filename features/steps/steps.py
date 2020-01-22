from behave import *

use_step_matcher("re")


@given('"(?P<page_name>.+)" page is open')
def step_impl(context, page_name):
    context.page_factory.get_page(page_name=page_name).open_self_page()


@then('I see an "(?P<page_name>.+)" page')
def step_impl(context, page_name):
    current_url = context.page_factory.get_page(page_name=page_name).get_page_url()
    expected_url = context.test_data.landing_page
    assert expected_url == current_url, \
        f'Invalid page address!\nGiven: {current_url},\nExpected: {expected_url}'
