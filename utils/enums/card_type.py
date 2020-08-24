from enum import Enum, auto


class CardType(Enum):
    AMEX = auto()
    VISA = auto()
    ASTROPAYCARD = auto()
    DINERS = auto()
    DISCOVER = auto()
    JCB = auto()
    MAESTRO = auto()
    MASTERCARD = auto()
    PIBA = auto()
    AMERICANEXPRESS = auto()

    @property
    def value(self) -> str:
        return self.name
