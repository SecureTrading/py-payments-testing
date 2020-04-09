from enum import Enum


class Config(Enum):
    BASE_CONFIG = "config.json"
    SUBMIT_ON_SUCCESS_AND_ERROR_TRUE = "configSubmitOnSuccessAndErrorTrue.json"
    ANIMATED_CARD = "configAnimatedCardTrue.json"
    UPDATE_JWT = "configUpdateJwtTrue.json"
    FIELD_STYLE = "configFieldStyle.json"
    IMMEDIATE_PAYMENT = "configImmediatePayment.json"
    SKIP_JSINIT = "configSkipJSinit.json"
    DEFER_INIT_START_ON_LOAD = "configStartOnLoadAndDeferInitTrue.json"
    SUBMIT_CVV_ONLY = "configSubmitCvvOnly.json"
    BYPASS_CARDS = "configBypassCards.json"
    INCORRECT_REQUEST_TYPE = "configIncorrectRequestType.json"
    PLACEHOLDERS = "configPlaceholders.json"
    NOTIFICATIONS_FALSE = "configNotificationsFalse.json"
    CYBERTONICA = "configCybertonica.json"
    CYBERTONICA_BYPASS_CARD = "configCybertonicaBypassCards.json"
    CYBERTONICA_IMMEDIATE_PAYMENT = "configCybertonicaImmediatePayment.json"
