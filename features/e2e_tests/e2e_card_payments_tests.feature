Feature: E2E Card Payments
  As a user
  I want to use card payments method
  In order to check full payment functionality

  @e2e_config_bypass_mastercard
  Scenario: Successful payment with bypassCard using Mastercard
    Given JS library is configured with BYPASS_MASTERCARD_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_for_bypass_cards
  Scenario: Successful payment bypass cards without 3d secure
    Given JS library is configured with BYPASS_CARDS_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_for_bypass_cards
  Scenario: Successful payment bypass cards with 3d secure
    Given JS library is configured with BYPASS_CARDS_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_AUTH_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_bypass_mastercard
  Scenario: Unsuccessful payment with bypassCard using Mastercard - invalid expiration date
    Given JS library is configured with BYPASS_MASTERCARD_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_INVALID_EXP_DATE_CARD
    And User clicks Pay button
    Then User will see payment status information: "Invalid field"
    And User will see that notification frame has "red" color
    And User will see that "EXPIRATION_DATE" field is highlighted
    And User will see "Invalid field" message under field: "EXPIRATION_DATE"

  @e2e_config_requesttypes_invalid_order
  Scenario: Unsuccessful payment with config's requestTypes param having values in invalid order
    Given JS library is configured with REQUEST_TYPES_CONFIG_INVALID_ORDER and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Invalid field"
    And User will see that notification frame has "red" color