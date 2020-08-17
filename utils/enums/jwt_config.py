from enum import Enum


class JwtConfig(Enum):
    BASE_JWT = "base_jwt_config.json"
    JWT_WITH_PAN = "jwt_config_with_pan.json"
    JWT_WITH_PARENT_TRANSACTION = "jwt_config_with_parenttransaction.json"
    JWT_VISA_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_visa_frictionless_with_parenttransaction.json"
    JWT_VISA_NON_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_visa_non_frictionless_with_parenttransaction.json"
    JWT_AMEX_NON_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_amex_non_frictionless_with_parenttransaction.json"
    JWT_WITH_SUBSCRIPTION = "jwt_config_with_subscription.json"
    JWT_WITH_CARD_DATA = "jwt_config_start_on_load_true.json"