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

    AMEX = '3400 000000 00611', '12/23', CardType.AMEX, 1234
    VISA = '4111 1100 0000 0211', '12/22', CardType.VISA, 123
    ASTROPAYCARD = '1801 0000 0000 0901', '12/23', CardType.ASTROPAYCARD, 123
    DINERS = '3000 000000 000111', '12/23', CardType.DINERS, 123
    DISCOVER = '6011 0000 0000 0301', '12/23', CardType.DISCOVER, 123
    JCB = '3528 0000 0000 0411', '12/23', CardType.JCB, 123
    MAESTRO = '5000 0000 0000 0611', '12/23', CardType.MAESTRO, 123
    MASTERCARD = '5100 0000 0000 0511', '12/23', CardType.MASTERCARD, 123

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
