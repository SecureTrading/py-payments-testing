from enum import Enum

from utils.date_util import convert_to_string, adjust_date_day, get_current_time, date_formats
from utils.enums.card_type import CardType


class Card(Enum):
    def __init__(self, formatted_number, expiration_date: str, card_type: CardType, cvv):
        self.formatted_number = formatted_number
        self.expiration_date = expiration_date
        self.type = card_type.name
        self.cvv = cvv

    # expiration date may be fixed value but if someone prefers more "dynamic" approach
    # there are 2 methods: future_expiration_date and past_expiration_date

    AMEX_CARD = '3400 000000 00611', '12/23', CardType.AMEX, 1234
    VISA_CARD = '4111 1100 0000 0211', '12/22', CardType.VISA, 123
    ASTROPAYCARD_CARD = '1801 0000 0000 0901', '12/23', CardType.ASTROPAYCARD, 123
    DINERS_CARD = '3000 000000 000111', '12/23', CardType.DINERS, 123
    DISCOVER_CARD = '6011 0000 0000 0301', '12/23', CardType.DISCOVER, 123
    JCB_CARD = '3528 0000 0000 0411', '12/23', CardType.JCB, 123
    MAESTRO_CARD = '5000 0000 0000 0611', '12/23', CardType.MAESTRO, 123
    MASTERCARD_CARD = '5100 0000 0000 0511', '12/23', CardType.MASTERCARD, 123
    MASTERCARD_SUCCESSFUL_AUTH_CARD = '52000 00000 0000 07', '01/23', CardType.MASTERCARD, 123
    VISA_FAILED_SIGNATURE_CARD = '4000 0000 0000 0010', '01/23', CardType.VISA, 123
    AMERICAN_EXPRESS_FAILED_AUTH_CARD = '3400 0000 0000 033', '01/23', CardType.AMERICANEXPRESS, 1234
    DISCOVER_PASSIVE_AUTH_CARD = '6011 0000 0000 0038', '01/23', CardType.DISCOVER, 123
    AMERICAN_EXPRESS_TIMEOUT_CARD = '3400 0000 0008 309', '01/23', CardType.AMERICANEXPRESS, 1234
    MASTERCARD_NOT_ENROLLED_CARD = '5200 0000 0000 0056', '01/23', CardType.MASTERCARD, 123
    AMERICAN_EXPRESS_UNAVAILABLE_CARD = '3400 0000 0007 780', '01/23', CardType.AMERICANEXPRESS, 1234
    VISA_MERCHANT_NOT_ACTIVE_CARD = '4000 0000 0000 0077', '01/23', CardType.VISA, 123
    VISA_CMPI_LOOKUP_ERROR_CARD = '4000 0000 0000 0085', '01/23', CardType.VISA, 123
    MASTERCARD_CMPI_AUTH_ERROR_CARD = '5200 0000 0000 0098', '01/23', CardType.MASTERCARD, 123
    MASTERCARD_AUTH_UNAVAILABLE_CARD = '5200 0000 0000 0031', '01/23', CardType.MASTERCARD, 123
    DISCOVER_BYPASSED_AUTH_CARD = '6011 9900 0000 0006', '01/23', CardType.DISCOVER, 123
    MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH = '5200 0000 0000 1005', '12/30', CardType.MASTERCARD, 123
    VISA_FAILED_FRICTIONLESS_AUTH = '4000 0000 0000 1018', '12/30', CardType.VISA, 123
    VISA_ATTEMPTS_STAND_IN_FRICTIONLESS_AUTH = '4000 0000 0000 1026', '12/30', CardType.VISA, 123
    MASTERCARD_UNAVAILABLE_FRICTIONLESS_AUTH = '5200 0000 0000 1039', '12/30', CardType.MASTERCARD, 123
    VISA_REJECTED_FRICTIONLESS_AUTH = '4000 0000 0000 1042', '12/30', CardType.VISA, 123
    MASTERCARD_AUTH_NOT_AVAILABLE_ON_LOOKUP = '5200 0000 0000 1054', '12/30', CardType.MASTERCARD, 123
    VISA_ERROR_ON_LOOKUP = '4000 0000 0000 1067', '12/30', CardType.VISA, 123
    VISA_TIMEOUT_ON_CMPI_LOOKUP_TRANSACTION = '4000 0000 0000 1075', '12/30', CardType.VISA, 123
    MASTERCARD_BYPASSED_AUTH = '5200 0000 0000 1088', '12/30', CardType.MASTERCARD, 123
    VISA_SUCCESSFUL_STEP_UP_AUTH = '4000 0000 0000 1091', '12/30', CardType.VISA, 123
    MASTERCARD_FAILED_STEP_UP_AUTH = '5200 0000 0000 1104', '12/30', CardType.MASTERCARD, 123
    VISA_STEP_UP_AUTH_IS_UNAVAILABLE = '4000 0000 0000 1117', '12/30', CardType.VISA, 123
    MASTERCARD_ERROR_ON_AUTH = '5200 0000 0000 1120', '12/30', CardType.MASTERCARD, 123
    MASTERCARD_PROMPT_FOR_WHITELIST = '5200 0000 0000 2003', '12/30', CardType.MASTERCARD, 123
    VISA_PRE_WHITELISTED_VISABASE_CONFIG = '4000 0000 0000 2016', '12/30', CardType.VISA, 123
    MASTERCARD_SUPPORT_TRANS_STATUS_I = '5200 0000 0000 2029', '12/30', CardType.MASTERCARD, 123

    @property
    def number(self):
        # the same number as the formatted one but with "normal" notation
        return int(self.formatted_number.replace(" ", ""))

    @property
    def value(self) -> str:
        return self.name

    @property
    def future_expiration_date(self) -> str:
        date_two_years_in_future = adjust_date_day(get_current_time(), 2 * 365)
        return convert_to_string(date_two_years_in_future, date_formats.month_year)

    @property
    def past_expiration_date(self) -> str:
        date_two_years_in_past = adjust_date_day(get_current_time(), -2 * 365)
        return convert_to_string(date_two_years_in_past, date_formats.month_year)
