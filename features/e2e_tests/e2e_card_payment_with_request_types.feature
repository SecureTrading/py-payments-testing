Feature: E2E Card Payments with request types in config

  As a user
  I want to use card payments method with request types config
  In order to check full payment functionality

  @reactJS
  @angular
  Scenario: Successful payment with config's requestTypes param having values in valid order
    Given JS library is configured with REQUEST_TYPE_ACC_TDQ_AUTH_RISK_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_requesttypes_invalid_order
  Scenario: Unsuccessful payment with config's requestTypes param having values in invalid order
    Given JS library is configured with REQUEST_TYPES_CONFIG_INVALID_ORDER and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Invalid field"
    And User will see that notification frame has "red" color

  @reactJS
  @angular
  Scenario: Successful payment with config's requestTypes ACCOUNTCHECK, TDQ, AUTH, SUBSCRIPTION
    Given JS library is configured with REQUEST_TYPE_ACHECK_TDQ_AUTH_SUB_CONFIG and JWT_WITH_SUBSCRIPTION
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color