from enum import Enum

from utils.date_util import convert_to_string, adjust_date_day, get_current_time, date_formats
from utils.enums.card_type import CardType


class Card(Enum):
    def __init__(self, formatted_number, expiration_date: str, card_type: CardType, cvv):
        self.formatted_number = formatted_number
        self.__expiration_date = expiration_date
        self.type = card_type.name
        self.cvv = cvv

    # by default expiration date will be future but it may be also fixed value
    # e.g. 11/22
    # or by using more descriptive value
    # like PAST / FUTURE
    # e.g. MASTERCARD_INVALID_EXP_DATE_CARD

    AMEX_CARD = '3400 000000 00611', '', CardType.AMEX, 1234
    VISA_CARD = '4111 1100 0000 0211', '', CardType.VISA, 123
    ASTROPAYCARD_CARD = '1801 0000 0000 0901', '', CardType.ASTROPAYCARD, 123
    DINERS_CARD = '3000 000000 000111', '', CardType.DINERS, 123
    DISCOVER_CARD = '6011 0000 0000 0301', '', CardType.DISCOVER, 123
    JCB_CARD = '3528 0000 0000 0411', '', CardType.JCB, 123
    MAESTRO_CARD = '5000 0000 0000 0611', '', CardType.MAESTRO, 123
    MASTERCARD_CARD = '5100 0000 0000 0511', '', CardType.MASTERCARD, 123
    MASTERCARD_DECLINED_CARD = '5100 0000 0000 0412', '', CardType.MASTERCARD, 123
    MASTERCARD_INVALID_EXP_DATE_CARD = '5100 0000 0000 0511', 'PAST', CardType.MASTERCARD, 123
    MASTERCARD_SUCCESSFUL_AUTH_CARD = '52000 00000 0000 07', '', CardType.MASTERCARD, 123
    VISA_FAILED_SIGNATURE_CARD = '4000 0000 0000 0010', '', CardType.VISA, 123
    AMERICAN_EXPRESS_FAILED_AUTH_CARD = '3400 0000 0000 033', '', CardType.AMERICANEXPRESS, 1234
    DISCOVER_PASSIVE_AUTH_CARD = '6011 0000 0000 0038', '', CardType.DISCOVER, 123
    AMERICAN_EXPRESS_TIMEOUT_CARD = '3400 0000 0008 309', '', CardType.AMERICANEXPRESS, 1234
    MASTERCARD_NOT_ENROLLED_CARD = '5200 0000 0000 0056', '', CardType.MASTERCARD, 123
    AMERICAN_EXPRESS_UNAVAILABLE_CARD = '3400 0000 0007 780', '', CardType.AMERICANEXPRESS, 1234
    VISA_MERCHANT_NOT_ACTIVE_CARD = '4000 0000 0000 0077', '', CardType.VISA, 123
    VISA_CMPI_LOOKUP_ERROR_CARD = '4000 0000 0000 0085', '', CardType.VISA, 123
    MASTERCARD_CMPI_AUTH_ERROR_CARD = '5200 0000 0000 0098', '', CardType.MASTERCARD, 123
    MASTERCARD_AUTH_UNAVAILABLE_CARD = '5200 0000 0000 0031', '', CardType.MASTERCARD, 123
    DISCOVER_BYPASSED_AUTH_CARD = '6011 9900 0000 0006', '', CardType.DISCOVER, 123
    MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH = '5200 0000 0000 1005', '', CardType.MASTERCARD, 123
    VISA_FAILED_FRICTIONLESS_AUTH = '4000 0000 0000 1018', '', CardType.VISA, 123
    MASTERCARD_UNAVAILABLE_FRICTIONLESS_AUTH = '5200 0000 0000 1039', '', CardType.MASTERCARD, 123
    VISA_REJECTED_FRICTIONLESS_AUTH = '4000 0000 0000 1042', '', CardType.VISA, 123
    MASTERCARD_AUTH_NOT_AVAILABLE_ON_LOOKUP = '5200 0000 0000 1054', '', CardType.MASTERCARD, 123
    VISA_ERROR_ON_LOOKUP = '4000 0000 0000 1067', '', CardType.VISA, 123
    VISA_TIMEOUT_ON_CMPI_LOOKUP_TRANSACTION = '4000 0000 0000 1075', '', CardType.VISA, 123
    MASTERCARD_BYPASSED_AUTH = '5200 0000 0000 1088', '', CardType.MASTERCARD, 123
    MASTERCARD_FAILED_STEP_UP_AUTH = '5200 0000 0000 1104', '', CardType.MASTERCARD, 123
    VISA_STEP_UP_AUTH_IS_UNAVAILABLE = '4000 0000 0000 1117', '', CardType.VISA, 123
    MASTERCARD_ERROR_ON_AUTH = '5200 0000 0000 1120', '', CardType.MASTERCARD, 123
    MASTERCARD_PROMPT_FOR_WHITELIST = '5200 0000 0000 2003', '', CardType.MASTERCARD, 123
    VISA_PRE_WHITELISTED_VISABASE_CONFIG = '4000 0000 0000 2016', '', CardType.VISA, 123
    MASTERCARD_SUPPORT_TRANS_STATUS_I = '5200 0000 0000 2029', '', CardType.MASTERCARD, 123
    MASTERCARD_STEP_UP_CARD = '5200 0000 0000 1096', '', CardType.MASTERCARD, 123
    VISA_FRICTIONLESS = '4000 0000 0000 1026', '', CardType.VISA, 123
    VISA_NON_FRICTIONLESS = '4000 0000 0000 1091', '', CardType.VISA, 123
    AMEX_NON_FRICTIONLESS = '3400 0000 0001 098', '', CardType.AMEX, 1234
    VISA_DECLINED_CARD = '4242 4242 4242 4242', '', CardType.VISA, 123

    @property
    def number(self):
        # the same number as the formatted one but with "normal" notation
        return int(self.formatted_number.replace(" ", ""))

    @property
    def value(self) -> str:
        return self.name

    @property
    def expiration_date(self) -> str:
        expiration_date: str = self.__expiration_date
        if not expiration_date or expiration_date.__eq__('FUTURE'):
            return self.future_expiration_date
        elif self.__expiration_date.__eq__('PAST'):
            return self.past_expiration_date
        return expiration_date

    @property
    def future_expiration_date(self) -> str:
        date_two_years_in_future = adjust_date_day(get_current_time(), 2 * 365)
        return convert_to_string(date_two_years_in_future, date_formats.month_year)

    @property
    def past_expiration_date(self) -> str:
        date_two_years_in_past = adjust_date_day(get_current_time(), -2 * 365)
        return convert_to_string(date_two_years_in_past, date_formats.month_year)
