import time

import ioc_config
from locators.animated_card_locators import AnimatedCardLocators
from locators.payment_methods_locators import PaymentMethodsLocators
from pages.base_page import BasePage
from utils.enums.field_type import FieldType
import json


class AnimatedCardPage(BasePage):

    def fill_payment_form_without_iframe(self, card_number, expiration, cvv):
        if "ie" in ioc_config.CONFIG.resolve('driver').browser:
            for digit in card_number:
                self._action.send_keys(AnimatedCardLocators.card_number_input_field, digit)
        else:
            self._action.send_keys(AnimatedCardLocators.card_number_input_field, card_number)
        self._action.send_keys(AnimatedCardLocators.expiration_date_input_field, expiration)
        if cvv is not None:
            self._action.send_keys(AnimatedCardLocators.security_code_input_field, cvv)

    def get_card_type_icon_from_animated_card(self):
        credit_card_icon = self._action.get_element_attribute(AnimatedCardLocators.card_type_logo_from_animated_card,
                                                              "alt")
        credit_card_icon = credit_card_icon.upper()
        return credit_card_icon

    def validate_credit_card_icon(self, expected_card_icon, is_field_in_iframe):
        if is_field_in_iframe:
            self._action.switch_to_iframe(FieldType.ANIMATED_CARD.value)
        actual_credit_card_icon = self.get_card_type_icon_from_animated_card()
        assert expected_card_icon in actual_credit_card_icon, f'Credit card icon is not correct, ' \
                                                              f'should be: "{expected_card_icon}" but is: "{actual_credit_card_icon}"'

    def get_data_from_animated_card(self, field_type, card_type):
        animated_card_data = ""
        if field_type == FieldType.CARD_NUMBER.name:
            animated_card_data = self._action.get_text(AnimatedCardLocators.credit_card_number_on_animated_card)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            animated_card_data = self._action.get_text(AnimatedCardLocators.expiration_date_on_animated_card)
        elif field_type == FieldType.SECURITY_CODE.name:
            if card_type == "AMEX":
                animated_card_data = self._action.get_text(AnimatedCardLocators.cvv_on_front_side_animated_card)
            else:
                animated_card_data = self._action.get_text(AnimatedCardLocators.cvv_on_back_side_animated_card)
        return animated_card_data

    def validate_data_on_animated_card(self, expected_data, field_type, card_type):
        actual_data_on_animated_card = self.get_data_from_animated_card(field_type, card_type)
        assert expected_data in actual_data_on_animated_card, f'Data on animated card is not correct, should be: ' \
                                                              f'"{expected_data}" but is: "{actual_data_on_animated_card}"'

    def validate_all_data_on_animated_card(self, card_number, exp_date, cvv, card_type, is_field_in_iframe):
        if is_field_in_iframe:
            self._action.switch_to_iframe(FieldType.ANIMATED_CARD.value)
        self.validate_data_on_animated_card(card_number, FieldType.CARD_NUMBER.name, card_type)
        self.validate_data_on_animated_card(exp_date, FieldType.EXPIRATION_DATE.name, card_type)
        if cvv is not None:
            self.validate_data_on_animated_card(cvv, FieldType.SECURITY_CODE.name, card_type)

    def validate_if_animated_card_is_flipped(self, card_type, is_field_in_iframe):
        if is_field_in_iframe:
            self._action.switch_to_iframe(FieldType.ANIMATED_CARD.value)
        animated_card_side = self._action.get_element_attribute(AnimatedCardLocators.animated_card, "class")
        if card_type == "AMEX":
            assert "flip-card" not in animated_card_side, f'Animated card is flipped for AMEX but should not be'
        else:
            assert "flip-card" in animated_card_side, f'Animated card is not flipped but should be'

    def change_field_focus(self):
        self._action.click(AnimatedCardLocators.card_number_input_field)

    def validate_if_no_iframe_field_is_highlighted(self, field_type):
        is_highlighted = self.is_field_highlighted(field_type)
        assert is_highlighted is True, f'{FieldType[field_type].name} field is not highlighted but should be'

    def is_field_highlighted(self, field_type):
        is_highlighted = False
        class_name = ""
        if field_type == FieldType.CARD_NUMBER.name:
            class_name = self._action.get_element_attribute(AnimatedCardLocators.card_number_input_field, "class")
        elif field_type == FieldType.EXPIRATION_DATE.name:
            class_name = self._action.get_element_attribute(AnimatedCardLocators.expiration_date_input_field, "class")
        elif field_type == FieldType.SECURITY_CODE.name:
            class_name = self._action.get_element_attribute(AnimatedCardLocators.security_code_input_field, "class")
        if "error" in class_name:
            is_highlighted = True
        return is_highlighted

    def validate_no_iframe_field_validation_message(self, field_type, expected_message):
        actual_message = self.get_field_validation_message(field_type)
        assert expected_message in actual_message, f'{FieldType[field_type].name} field validation message is not correct, ' \
                                                   f'should be: "{expected_message}" but is: "{actual_message}"'

    def get_field_validation_message(self, field_type):
        validation_message = ""
        if field_type == FieldType.CARD_NUMBER.name:
            validation_message = self._action.get_text(AnimatedCardLocators.card_number_field_validation_message)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            validation_message = self._action.get_text(AnimatedCardLocators.expiration_date_field_validation_message)
        elif field_type == FieldType.SECURITY_CODE.name:
            validation_message = self._action.get_text(AnimatedCardLocators.security_code_field_validation_message)
        return validation_message

    def validate_animated_card_translation(self, language, is_field_in_iframe):
        self.validate_animated_card_element_translation(AnimatedCardLocators.card_number_label,
                                                        language, "Card number", is_field_in_iframe)
        self.validate_animated_card_element_translation(AnimatedCardLocators.expiration_date_label,
                                                        language, "Expiration date", is_field_in_iframe)
        self.validate_animated_card_element_translation(AnimatedCardLocators.security_code_label,
                                                        language, "Security code", is_field_in_iframe)

    def validate_animated_card_element_translation(self, element, language, key, is_field_in_iframe):
        actual_translation = self.get_animated_card_label_translation(element, is_field_in_iframe)
        expected_translation = self.get_translation_from_json(language, key)
        if "safari" not in ioc_config.CONFIG.resolve('driver').browser:
            expected_translation = expected_translation.upper()
        assert actual_translation in expected_translation, f"Translation is not correct: " \
                                                           f"should be {expected_translation} but is {actual_translation}"

    def get_animated_card_label_translation(self, locator, is_field_in_iframe):
        if is_field_in_iframe:
            self._action.switch_to_iframe(FieldType.ANIMATED_CARD.value)
        element_translation = self._action.get_text(locator)
        return element_translation

    def get_translation_from_json(self, language, key):
        with open(f'resources/languages/{language}.json', 'r') as f:
            translation = json.load(f)
        return translation[key]

    def is_field_displayed(self, field_type):
        is_displayed = False
        if field_type == FieldType.CARD_NUMBER.name:
            is_displayed = self._action.is_element_displayed(AnimatedCardLocators.card_number_input_field)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            is_displayed = self._action.is_element_displayed(AnimatedCardLocators.expiration_date_input_field)
        elif field_type == FieldType.SECURITY_CODE.name:
            is_displayed = self._action.is_element_displayed(AnimatedCardLocators.security_code_input_field)
        elif field_type == FieldType.SUBMIT_BUTTON.name:
            is_displayed = self._action.is_element_displayed(PaymentMethodsLocators.pay_mock_button)
        return is_displayed

    def is_field_enabled(self, field_type):
        is_enabled = False
        if field_type == FieldType.CARD_NUMBER.name:
            is_enabled = self._action.is_element_enabled(AnimatedCardLocators.card_number_input_field)
        elif field_type == FieldType.EXPIRATION_DATE.name:
            is_enabled = self._action.is_element_enabled(AnimatedCardLocators.expiration_date_input_field)
        elif field_type == FieldType.SECURITY_CODE.name:
            is_enabled = self._action.is_element_enabled(AnimatedCardLocators.security_code_input_field)
        return is_enabled

    def validate_if_field_is_disabled(self, field_type):
        is_enabled = self.is_field_enabled(field_type)
        assert is_enabled is False, f'{FieldType[field_type].name} field is not disabled but should be'