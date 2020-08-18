from enum import Enum


class JwtConfig(Enum):
    BASE_JWT = "base_jwt_config.json"
    BASE_UPDATED_JWT = "base_jwt__updated_config.json"
    JWT_WITH_PAN = "jwt_config_with_pan.json"
    JWT_WITH_PARENT_TRANSACTION = "jwt_config_with_parenttransaction.json"
    JWT_VISA_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_visa_frictionless_with_parenttransaction.json"
    JWT_VISA_NON_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_visa_non_frictionless_with_parenttransaction.json"
    JWT_AMEX_NON_FRICTIONLESS_PARENT_TRANSACTION = "jwt_config_amex_non_frictionless_with_parenttransaction.json"
    JWT_WITH_SUBSCRIPTION = "jwt_config_with_subscription.json"
    JWT_WITH_NON_FRICTIONLESS_CARD = "jwt_config_non_frictionless_card.json"
    JWT_WITH_FRICTIONLESS_CARD = "jwt_config_frictionless_card.json"
    JWT_NON_FRICTIONLESS_CARD_SUBSCRIPTION = "jwt_config_non_frictionless_card_subscription.json"