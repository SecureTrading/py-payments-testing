from enum import Enum


class e2eConfig(Enum):
    BASIC_CONFIG = "e2eBasicConfig.json"
    BYPASS_MASTERCARD_CONFIG = "e2eConfigBypassMastercard.json"
    CYBERTONICA_CONFIG = "e2eConfigCybertonica.json"
    CYBERTONICA_WITH_BYPASSCARDS_CONFIG = "e2eConfigCybertonicaWithBypass.json"
    CYBERTONICA_START_ON_LOAD_CONFIG = "e2eConfigCybertonicaStartOnLoadTrue.json"
    BYPASS_CARDS_CONFIG = "e2eConfigForBypassCards.json"
    START_ON_LOAD_CONFIG = "e2eConfigStartOnLoadTrue.json"
    START_ON_LOAD_REQUEST_TYPES_CONFIG = "e2eConfigStartOnLoadRequestTypes.json"
    START_ON_LOAD_REQUEST_TYPES_SUB_CONFIG = "e2eConfigStartOnLoadRequestTypesSub.json"
    SUBMIT_ON_ERROR_CONFIG = "e2eConfigSubmitOnError.json"
    SUBMIT_ON_SUCCESS_CONFIG = "e2eConfigSubmitOnSuccess.json"
    SUBMIT_ON_SUCCESS_SECURITY_CODE_CONFIG = "e2eConfigSubmitOnSuccessSecurityCode.json"
    DEFER_INIT_CONFIG = "e2eConfigSubmitOnSuccessSecurityCode.json"
    TOKENISATION_CONFIG = "e2eForTokenisation.json"
    REQUEST_TYPES_CONFIG = "e2eConfigRequestTypes.json"
    VISA_CHECKOUT_CONFIG = "e2eConfigVisaCheckout.json"
    VISA_CHECKOUT_WITH_SUBMIT_ON_SUCCESS_CONFIG = "e2eConfigVisaCheckoutWithSubmitOnSuccess.json"
    VISA_CHECKOUT_WITH_CYBERTONICA_CONFIG = "e2eConfigVisaCheckoutWithCybertonica.json"
    VISA_CHECKOUT_WITH_DEFERINIT_TRUE_CONFIG = "e2eConfigVisaCheckoutWithDeferInitTrue.json"
    VISA_CHECKOUT_WITH_REQUEST_TYPES_CONFIG = "e2eConfigVisaCheckoutWithRequestTypes.json"