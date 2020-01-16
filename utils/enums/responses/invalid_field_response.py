from enum import Enum


class InvalidFieldResponse(Enum):
    CARD_NUMBER = "numberInvalidField.json"
    EXPIRATION_DATE = "expiryDateInvalidField.json"
    SECURITY_CODE = "cvvInvalidField.json"
    EMAIL = "emailInvalidField.json"
