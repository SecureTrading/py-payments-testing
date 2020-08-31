from behave import step, use_step_matcher

from utils.enums.card import Card
from utils.enums.visa_checkout_field import VisaCheckoutField

use_step_matcher("re")

@step("User clicks on Visa Checkout button")
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.click_visa_checkout_button()


@step('User fills visa checkout email address')
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.fill_selected_field(VisaCheckoutField.EMAIL_ADDRESS.name)
    visa_checkout_page.click_continue_checkout_process()


@step('User fills visa checkout one time password')
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.fill_selected_field(VisaCheckoutField.ONE_TIME_PASSWORD.name)


@step("User confirms displayed card with data")
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.click_continue_visa_payment_process()


@step('User selects (?P<card>.+) card on visa checkout popup')
def step_impl(context, card: Card):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    card = Card.__members__[card]
    visa_checkout_page.select_card_by_ending_number(card.formatted_number[-4:])


@step('User closes the visa checkout popup')
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.click_visa_checkout_close_button()


@step("User confirms visa checkout security code")
def step_impl(context):
    visa_checkout_page = context.page_factory.get_page(page_name='visa_checkout')
    visa_checkout_page.is_security_code_displayed()