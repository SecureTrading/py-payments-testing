from enum import Enum


class Config(Enum):
    BASE_CONFIG = "config.json"
    SUBMIT_ON_SUCCESS_TRUE = "configSubmitOnSuccessTrue.json"
    ANIMATED_CARD = "configAnimatedCardTrue.json"
    UPDATE_JWT = "configUpdateJwtTrue.json"
    FIELD_STYLE = "configFieldStyle.json"
    IMMEDIATE_PAYMENT = "configImmediatePayment.json"
    SKIP_JSINIT = "configSkipJSinit.json"
    DEFER_INIT_START_ON_LOAD = "configStartOnLoadAndDeferInitTrue.json"
    SUBMIT_CVV_ONLY = "configSubmitCvvOnly.json"
    BYPASS_CARDS = "configBypassCards.json"
    INCORRECT_REQUEST_TYPE = 'config_incorrect_request_type.json'
