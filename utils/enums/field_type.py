from enum import Enum


class FieldType(Enum):
    ALL = "all"
    CARD_NUMBER = "st-card-number-iframe"
    EXPIRATION_DATE = "st-expiration-date-iframe"
    SECURITY_CODE = "st-security-code-iframe"
    ANIMATED_CARD = "st-animated-card-iframe"
    NOTIFICATION_FRAME = "st-notification-frame-iframe"
    CONTROL_IFRAME = "st-control-frame-iframe"
    CT_FRAME = "Cardinal-collector"
    CARDINAL_IFRAME = "Cardinal-CCA-IFrame"
    PARENT_IFRAME = "st-parent-frame"
    V1_PARENT_IFRAME = "authWindow"
    VISA_CHECKOUT = 'vcop-src-frame'
    SUBMIT_BUTTON = 1
    NAME = 2
    EMAIL = 3
    PHONE = 4
    CARD_ICON = 5
