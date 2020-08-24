from behave import *

use_step_matcher("re")


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