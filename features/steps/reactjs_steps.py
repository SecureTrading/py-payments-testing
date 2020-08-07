import time

from behave import *

from configuration import CONFIGURATION

use_step_matcher("re")


@step("User opens reactjs app page with payment form")
def step_impl(context):
    reactjs_page = context.page_factory.get_page(page_name='reactjs')
    reactjs_page.open_page(CONFIGURATION.URL.REACT_APP)
    reactjs_page.is_connection_not_private_dispayed(CONFIGURATION.URL.REACT_APP)
    reactjs_page.wait_for_iframe()


@step('Notification message with (?P<payment_status_message>.+) text is displayed')
def step_impl(context, payment_status_message):
    reactjs_page = context.page_factory.get_page(page_name='reactjs')
    reactjs_page.validate_notofication_message(payment_status_message)


@step('User switch tab to \'Personal Data\' in reactjs app')
def step_impl(context):
    reactjs_page = context.page_factory.get_page(page_name='reactjs')
    reactjs_page.click_personal_data_tab()


@step('User switch tab to \'Home\' in reactjs app')
def step_impl(context):
    reactjs_page = context.page_factory.get_page(page_name='reactjs')
    reactjs_page.click_home_tab()


@step('User switch tab to \'Payment\' in reactjs app')
def step_impl(context):
    reactjs_page = context.page_factory.get_page(page_name='reactjs')
    reactjs_page.click_home_tab()