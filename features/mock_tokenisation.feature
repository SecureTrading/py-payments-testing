Feature: Tokenisation

  As a user
  I want to use card payments method with tokenisation config
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_tokenisation_visa @extended_tests_part_2
  Scenario: Tokenisation - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenisation_amex
  Scenario: Tokenisation - successful payment by AMEX card
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenisation_visa_defer_init
  Scenario: Tokenisation with deferInit - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenisation_amex_defer_init
  Scenario: Tokenisation with deferInit - successful payment by AMEX card
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once

  @config_tokenisation_bypass_cards_visa
  Scenario: Tokenisation and bypassCard - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was not sent
    And AUTH request was sent only once

  @config_tokenisation_visa_request_types
  Scenario: Tokenisation - successful payment by VISA with request types: RISKDEC, ACCOUNTCHECK, TDQ, AUTH
    When User fills "SECURITY_CODE" field "123"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once