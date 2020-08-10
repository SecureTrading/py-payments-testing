from enum import Enum


class e2eConfig(Enum):
    BASIC_CONFIG = "e2eBasicConfig.json"
    BYPASS_MASTERCARD_CONFIG = "e2eConfigBypassMastercard.json"
    CYBERTONICA_CONFIG = "e2eConfigCybertonica.json"
    CYBERTONICA_WITH_BYPASSCARDS_CONFIG = "e2eConfigCybertonicaWithBypass.json"
    BYPASS_CARDS_CONFIG = "e2eConfigForBypassCards.json"
    START_ON_LOAD_CONFIG = "e2eConfigStartOnLoadTrue.json"
    SUBMIT_ON_ERROR_CONFIG = "e2eConfigSubmitOnError.json"
    SUBMIT_ON_SUCCESS_CONFIG = "e2eConfigSubmitOnSuccess.json"
    SUBMIT_ON_SUCCESS_SECURITY_CODE_CONFIG = "e2eConfigSubmitOnSuccessSecurityCode.json"
    DEFER_INIT_CONFIG = "e2eConfigSubmitOnSuccessSecurityCode.json"
    TOKENISATION_CONFIG = "e2eForTokenisation.json"