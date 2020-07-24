from behave import *

from utils.enums.card import Card
from utils.enums.card_type import CardType

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


@when('User fills payment form with defined card (?P<card_type>.+)')
def step_impl(context, card_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    for card in Card:
        if card.name == card_type:
            payment_page.fill_payment_form(card.number, card.future_expiration_date, card.cvv)
            break

