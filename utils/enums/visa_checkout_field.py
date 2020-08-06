from enum import Enum, auto


class VisaCheckoutField(Enum):
    EMAIL_ADDRESS = auto()
    ONE_TIME_PASSWORD = auto()

    @property
    def value(self) -> str:
        return self.name