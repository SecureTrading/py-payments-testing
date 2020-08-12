from behave import step, use_step_matcher

from utils.enums.visa_checkout_field import VisaCheckoutField

use_step_matcher("re")

@step("User clicks on Visa Checkout button")
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.click_visa_checkout_button()


@step('User fills visa checkout EMAIL_ADDRESS')
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    field = VisaCheckoutField.EMAIL_ADDRESS
    visa_checkout_page.fill_selected_field(field.name)
    visa_checkout_page.click_continue_checkout_process()


@step('User fills visa checkout ONE_TIME_PASSWORD')
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    field = VisaCheckoutField.ONE_TIME_PASSWORD
    visa_checkout_page.fill_selected_field(field.name)


@step("User confirm displayed card with data")
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.click_continue_visa_payment_process()