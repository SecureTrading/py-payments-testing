from enum import Enum


class FieldType(Enum):
    CARD_NUMBER = "st-card-number-iframe"
    EXPIRATION_DATE = "st-expiration-date-iframe"
    SECURITY_CODE = "st-security-code-iframe"
    ANIMATED_CARD = "st-animated-card-iframe"
    NOTIFICATION_FRAME = "st-notification-frame-iframe"
    PARENT_IFRAME = "st-parent-frame"
    SUBMIT_BUTTON = 1
    NAME = 2
    EMAIL = 3
    PHONE = 4
    CARD_ICON = 5
