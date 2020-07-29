from enum import Enum


class JwtConfig(Enum):
    BASE_JWT = "base_jwt_config.json"
    JWT_WITH_PAN = "jwt_config_with_pan.json"
    JWT_WITH_PARENT_TRANSACTION = "jwt_config_with_parenttransaction.json"
    JWT_WITH_SUBSCRIPTION = "jwt_config_with_subscription.json"