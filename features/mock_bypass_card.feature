Feature: Bypass Cards config

  As a user
  I want to use card payments method with bypass config
  In order to check payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_bypass_cards @bypass_cards
  Scenario Outline: Bypass Cards - Successful payment by <card_type>
    When User fills payment form with credit card number "<card_number>", expiration date "12/30" and cvv "<cvv>"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH request was sent only once with correct data
    Examples:
      | card_number      | cvv  | card_type  |
      | 4111110000000211 | 123  | VISA       |
      | 340000000000611  | 1234 | AMEX       |
      | 6011000000000301 | 123  | DISCOVER   |
      | 3528000000000411 | 123  | JCB        |
      | 5000000000000611 | 123  | MAESTRO    |
      | 5100000000000511 | 123  | MASTERCARD |
      | 3000000000000111 | 123  | DINERS     |

  @config_bypass_cards
  Scenario: Bypass Cards - Successful payment by PIBA
    When User fills payment form with credit card number "3089500000000000021", expiration date "12/23"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH request was sent only once

  @config_bypass_cards_auth
  Scenario: Successful payment with bypassCard and custom request types: AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH ware sent only once in one request

  @config_bypass_cards_tdq_auth
  Scenario: Successful payment with bypassCard and custom request types: THREEDQUERY, AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH ware sent only once in one request

  @config_bypass_cards_acheck_tdq_auth_subscription
  Scenario: Successful payment with bypassCard and custom request types: ACCOUNTCHECK, THREEDQUERY, AUTH, SUBSCRIPTION
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - ACCOUNTCHECK, AUTH, SUBSCRIPTION response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And ACCOUNTCHECK, AUTH, SUBSCRIPTION ware sent only once in one request

  @config_bypass_cards_acheck_tdq_auth
  Scenario: Successful payment with bypassCard and custom request types: ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - ACCOUNTCHECK, AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And ACCOUNTCHECK, AUTH ware sent only once in one request

  @config_bypass_cards_riskdec_acheck_tdq_auth
  Scenario: Successful payment with bypassCard and custom request types: RISKDEC, ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - RISKDEC, ACCOUNTCHECK, AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And RISKDEC, ACCOUNTCHECK, AUTH ware sent only once in one request

  @config_bypass_cards_tdq_auth_riskdec
  Scenario: Successful payment with bypassCard and custom request types: THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH, RISKDEC ware sent only once in one request

  @config_bypass_cards_tdq_acheck_riskdec_auth
  Scenario: Invalid payment with bypassCard and custom request types: THREEDQUERY, ACCOUNTCHECK, RISKDEC, AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button - ACCOUNTCHECK, RISKDEC, AUTH response is set to "OK"
    And User will see payment status information: "Invalid field"
    And User will see that notification frame has "red" color
    And THREEDQUERY request was not sent
    And ACCOUNTCHECK, RISKDEC, AUTH ware sent only once in one request