import time

from assertpy import soft_assertions
from behave import use_step_matcher, step, when, then, given
from configuration import CONFIGURATION
from utils.configurations.inline_config_generator import create_inline_config
from utils.configurations.jwt_generator import encode_jwt_for_json
from utils.dict.url_after_redirection import url_after_redirection
from utils.enums.e2e_config import e2eConfig
from utils.enums.example_page import ExamplePage
from utils.enums.field_type import FieldType
from utils.enums.jwt_config import JwtConfig
from utils.enums.payment_type import PaymentType
from utils.enums.request_type import RequestType
from utils.enums.responses.invalid_field_response import InvalidFieldResponse
from utils.mock_handler import stub_st_request_type, MockUrl

use_step_matcher("re")


@step("User opens page with payment form")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' not in context.scenario.tags[0] and 'parent_iframe' not in context.scenario.tags and \
            'config_cybertonica_immediate_payment' not in context.scenario.tags:
        if ('safari' in context.browser) or ('iP' in CONFIGURATION.REMOTE_DEVICE):
            payment_page.open_page(MockUrl.WEBSERVICES_DOMAIN.value)
            if 'safari' in context.browser or 'visa_test' in context.scenario.tags or 'apple_test' in context.scenario.tags:
                payment_page.open_page(MockUrl.THIRDPARTY_URL.value)
        payment_page.open_page(CONFIGURATION.URL.BASE_URL)
        payment_page.is_connection_not_private_dispayed(CONFIGURATION.URL.BASE_URL)
        payment_page.wait_for_iframe()


@when(
    'User fills payment form with credit card number "(?P<card_number>.+)", expiration date "(?P<exp_date>.+)" and cvv "(?P<cvv>.+)"')
def step_impl(context, card_number, exp_date, cvv):
    context.pan = card_number
    context.exp_date = exp_date
    context.cvv = cvv
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form(card_number, exp_date, cvv)


@step('User will see payment status information: "(?P<payment_status_message>.+)"')
def step_impl(context, payment_status_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'switch_to_parent_iframe' in context.scenario.tags:
        payment_page.switch_to_parent_iframe()
    payment_page.validate_payment_status_message(payment_status_message)


@step('User will see that notification frame has "(?P<color>.+)" color')
def step_impl(context, color):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_notification_frame_color(color)


@step("User clicks Pay button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@step("User clicks Additional button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.click_additional_btn()


@step("User accept success alert")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.accept_alert()


@then('User will see validation message "(?P<expected_message>.+)" under all fields')
def step_impl(context, expected_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_field_validation_message(FieldType.CARD_NUMBER.name, expected_message)
    payment_page.validate_field_validation_message(FieldType.EXPIRATION_DATE.name, expected_message)
    payment_page.validate_field_validation_message(FieldType.SECURITY_CODE.name, expected_message)


@step("User will see that all fields are highlighted")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_highlighted(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_highlighted(FieldType.EXPIRATION_DATE.name)
    payment_page.validate_if_field_is_highlighted(FieldType.SECURITY_CODE.name)


@when(
    'User fills payment form with incorrect or missing data: card number "(?P<card_number>.+)",'
    ' expiration date "(?P<exp_date>.+)" and cvv "(?P<cvv>.+)"')
def step_impl(context, card_number, exp_date, cvv):
    context.pan = card_number
    context.exp_date = exp_date
    context.cvv = cvv
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form(card_number, exp_date, cvv)


@step('User will see "(?P<expected_message>.+)" message under field: "(?P<field>.+)"')
def step_impl(context, expected_message, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_field_validation_message(FieldType[field].name, expected_message)


@step('User will see that "(?P<field>.+)" field is highlighted')
def step_impl(context, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_highlighted(FieldType[field].name)


@step('InvalidField response set for "(?P<field>.+)"')
def step_impl(context, field):
    stub_st_request_type(InvalidFieldResponse[field].value, RequestType.THREEDQUERY.name)


@then('User will see notification frame with message: "(?P<expected_message>.+)"')
def step_impl(context, expected_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_payment_status_message(expected_message)


@when('User chooses (?P<payment_method>.+) as payment method')
def step_impl(context, payment_method):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.choose_payment_methods(PaymentType[payment_method].name)


@then('User will see that Submit button is "(?P<form_status>.+)" after payment')
def step_impl(context, form_status):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    time.sleep(1)
    payment_page.validate_form_status(FieldType.SUBMIT_BUTTON.name, form_status)


@step('User will see that (?P<field>.+) input fields are "(?P<form_status>.+)"')
def step_impl(context, field: FieldType, form_status):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    field = FieldType.__members__[field]
    if field.name == "ALL":
        payment_page.validate_form_status(FieldType.SECURITY_CODE.name, form_status)
        payment_page.validate_form_status(FieldType.CARD_NUMBER.name, form_status)
        payment_page.validate_form_status(FieldType.EXPIRATION_DATE.name, form_status)
    else:
        payment_page.validate_form_status(field.name, form_status)


@when('User fills "(?P<field>.+)" field "(?P<value>.+)"')
def step_impl(context, field, value):
    context.cvv = value
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_credit_card_field(FieldType[field].name, value)


@then('User will see that "(?P<field>.+)" field has correct style')
def step_impl(context, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if field == FieldType.CARD_NUMBER.name:
        payment_page.validate_css_style(FieldType.CARD_NUMBER.name, "background-color", '100, 149, 237')
    elif field == FieldType.EXPIRATION_DATE.name:
        payment_page.validate_css_style(FieldType.EXPIRATION_DATE.name, "background-color", '143, 188, 143')
    elif field == FieldType.SECURITY_CODE.name:
        payment_page.validate_css_style(FieldType.SECURITY_CODE.name, "background-color", '255, 243, 51')
    if field == FieldType.NOTIFICATION_FRAME.name:
        payment_page.validate_css_style(FieldType.NOTIFICATION_FRAME.name, "background-color", '100, 149, 237')


@when('User changes page language to "(?P<language>.+)"')
def step_impl(context, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    jwt = payment_page.get_translation_from_json(language, "jwt")
    payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}?jwt={jwt}")
    context.executor.wait_for_javascript()


@then('User will see all labels displayed on page translated into "(?P<language>.+)"')
def step_impl(context, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_labels_translation(language)


@step('User will see validation message "(?P<key>.+)" under all fields translated into "(?P<language>.+)"')
def step_impl(context, key, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_message_translation_under_field(FieldType.CARD_NUMBER.name, language, key)
    payment_page.validate_message_translation_under_field(FieldType.EXPIRATION_DATE.name, language, key)
    payment_page.validate_message_translation_under_field(FieldType.SECURITY_CODE.name, language, key)


@then(
    'User will see validation message "(?P<key>.+)" under "(?P<field>.+)" field translated into (?P<language>.+)')
def step_impl(context, key, field, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_message_translation_under_field(FieldType[field].name, language, key)


@then('User will see "(?P<key>.+)" payment status translated into "(?P<language>.+)"')
def step_impl(context, key, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_payment_status_translation(language, key)


@step("User opens payment page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'safari' in context.browser or ('iP' in CONFIGURATION.REMOTE_DEVICE):
        payment_page.open_page(MockUrl.WEBSERVICES_DOMAIN.value)
        payment_page.open_page(MockUrl.THIRDPARTY_URL.value)
        context.executor.wait_for_javascript()
        payment_page.wait_for_iframe()
    if 'parent_iframe' in context.scenario.tags:
        payment_page.open_page(CONFIGURATION.URL.BASE_URL + '/iframe.html')
        payment_page.switch_to_parent_iframe()
        payment_page.wait_for_iframe()
    else:
        payment_page.open_page(CONFIGURATION.URL.BASE_URL)


@then("User is redirected to action page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    time.sleep(1)
    for key, value in url_after_redirection.items():
        if key in context.scenario.name:
            if "Cardinal Commerce - successful" in key and 'IE' in CONFIGURATION.REMOTE_BROWSER:
                payment_page.validate_if_url_contains_info_about_payment(url_after_redirection['IE - success'])
            elif "Cardinal Commerce - error" in key and 'IE' in CONFIGURATION.REMOTE_BROWSER:
                payment_page.validate_if_url_contains_info_about_payment(url_after_redirection['IE - error'])
            else:
                payment_page.validate_if_url_contains_info_about_payment(value)
                break


@step('User will be sent to page with url "(?P<url>.+)" having params')
def step_impl(context, url: str):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    wait_for_url = True
    # if "update_jwt_test" in context.scenario.tags:
    #     wait_for_url = True
    with soft_assertions():
        payment_page.validate_base_url(url, wait_for_url)
        for param in context.table:
            payment_page.validate_if_url_contains_param(param['key'], param['value'])


@when('User fills payment form with credit card number "(?P<card_number>.+)", expiration date "(?P<exp_date>.+)"')
def step_impl(context, card_number, exp_date):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form_without_cvv(card_number, exp_date)


@step("User calls updateJWT function by filling amount field")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_amount_field('1')


@then('User will see that "(?P<field_type>.+)" field is disabled')
def step_impl(context, field_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_disabled(field_type)


@step('User will see "(?P<callback_popup>.+)" popup')
def step_impl(context, callback_popup):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_callback_popup_is_displayed(callback_popup)


@then("User will see that application is not fully loaded")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_not_displayed(FieldType.EXPIRATION_DATE.name)


@then("User will see (?P<placeholders>.+) placeholders in input fields: (?P<card>.+), (?P<date>.+), (?P<cvv>.+)")
def step_impl(context, placeholders, card, date, cvv):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if placeholders == "specific":
        payment_page.validate_placeholders(card, date, cvv)
    if placeholders == "default":
        payment_page.validate_placeholders(card, date, cvv)


@then("User will see '\*\*\*\*' placeholder in security code field")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_placeholder(FieldType.SECURITY_CODE.name, "****")


@then('User will see "(?P<card_type>.+)" icon in card number input field')
def step_impl(context, card_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_credit_card_icon_in_input_field(card_type)


@then("User will not see notification frame")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType.NOTIFICATION_FRAME.name)


@when('User fills merchant data with name "(?P<name>.+)", email "(?P<email>.+)", phone "(?P<phone>.+)"')
def step_impl(context, name, email, phone):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_merchant_form(name, email, phone)


@then("User will not see (?P<field_type>.+)")
def step_impl(context, field_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType[field_type].name)


@step("User press enter button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.press_enter_button_on_security_code_field()


@step("User fills (?P<auth_type>.+) authentication modal")
def step_impl(context, auth_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_cardinal_authentication_code(auth_type)
    if 'parent_iframe' in context.scenario.tags:
        payment_page.switch_to_parent_iframe()


@step("User will see the same provided data in inputs fields")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_value_of_input_field(FieldType.CARD_NUMBER.name, "5200 0000 0000 1005")
    payment_page.validate_value_of_input_field(FieldType.EXPIRATION_DATE.name, context.exp_date)
    payment_page.validate_value_of_input_field(FieldType.SECURITY_CODE.name, context.cvv)


@step("User will see correct error code displayed in popup")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_callback_with_data_type("Error code: OK")


@then("User remains on checkout page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_base_url(CONFIGURATION.URL.BASE_URL[8:], False)


@given('JS library is configured with (?P<e2e_config>.+) and (?P<jwt_config>.+)')
def step_impl(context, e2e_config: e2eConfig, jwt_config: JwtConfig):
    jwt = encode_jwt_for_json(JwtConfig[jwt_config])
    context.inline_config = create_inline_config(e2eConfig[e2e_config], jwt)


@step("User opens prepared payment form page (?P<example_page>.+)")
def step_impl(context, example_page: ExamplePage):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if "WITH_UPDATE_JWT" in example_page:
        jwt = ''
        for row in context.table:
            jwt = encode_jwt_for_json(JwtConfig[f"{row['jwtName']}"])
        payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value % jwt}")
        context.test_data.update_jwt = jwt  # test data replaced to check required value in assertion
    else:
        payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value}")
    payment_page.wait_for_iframe()


@step("User opens (?:example page|example page (?P<example_page>.+))")
def step_impl(context, example_page: ExamplePage):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    # setting url specific params accordingly to example page
    if example_page is None:
        url = f"{CONFIGURATION.URL.BASE_URL}/?{context.inline_config}"
    elif "IN_IFRAME" in example_page:
        url = f"{CONFIGURATION.URL.BASE_URL}/{ExamplePage[example_page].value}{context.inline_config}"
    elif "WITH_UPDATE_JWT" in example_page:
        jwt = ''
        for row in context.table:
            jwt = encode_jwt_for_json(JwtConfig[f"{row['jwtName']}"])
        url = f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value % jwt}{context.inline_config}"
    else:
        url = f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value}&{context.inline_config}"
    url = url.replace("??", "?").replace("&&", "&")  # just making sure some elements are not duplicated

    payment_page.open_page(url)

    if example_page is not None and "IN_IFRAME" in example_page:
        payment_page.switch_to_parent_iframe()
    payment_page.wait_for_iframe()


@then('User will see that (?P<element>.+) is translated into "(?P<expected_value>.+)"')
def step_impl(context, element, expected_value):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if element in "Pay button":
        payment_page.validate_element_specific_translation(FieldType.SUBMIT_BUTTON.name, expected_value)
    else:
        payment_page.validate_element_specific_translation(FieldType.CARD_NUMBER.name, expected_value)
        payment_page.validate_element_specific_translation(FieldType.EXPIRATION_DATE.name, expected_value)


@step('"(?P<callback_popup>.+)" callback is called only once')
def step_impl(context, callback_popup):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_in_callback_counter_popup(callback_popup)


@then('User will see that (?P<field_type>.+) field has (?P<rgb_color>.+) color')
def step_impl(context, field_type, rgb_color):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_css_style(FieldType[field_type].name, "background-color", rgb_color)
