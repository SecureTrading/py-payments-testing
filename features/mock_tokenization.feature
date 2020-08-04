Feature: Tokenization

  As a user
  I want to use card payments method with tokenization config
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_tokenization_visa @extended_tests_part_2
  Scenario: Tokenization - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenization_amex
  Scenario: Tokenization - successful payment by AMEX card
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenization_visa_defer_init
  Scenario: Tokenization with deferInit - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenization_amex_defer_init
  Scenario: Tokenization with deferInit - successful payment by AMEX card
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once

  @config_tokenization_bypass_cards_visa
  Scenario: Tokenization and bypassCard - successful payment by VISA card
    When User fills "SECURITY_CODE" field "123"
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was not sent
    And AUTH request was sent only once