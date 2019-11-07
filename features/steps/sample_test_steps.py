from behave import *

use_step_matcher("re")

@then('the title should contain "(?P<title>.+)"')
def step_impl(context, title):
    sample_page = context.page_factory.get_page(page_name='sample')
    browser_title = sample_page.get_page_title()
    assert title in browser_title, f'Found "{browser_title}" instead'