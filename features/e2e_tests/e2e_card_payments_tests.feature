Feature: E2E Card Payments
  As a user
  I want to use card payments method
  In order to check full payment functionality

  @reactJS
  @angular
  @e2e_config_bypass_mastercard
  Scenario: Successful payment with bypassCard using Mastercard
    Given JS library is configured with BYPASS_MASTERCARD_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_AUTH_CARD
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

  @e2e_config_bypass_maestro
  Scenario: Unsuccessful payment with bypassCard using Maestro - invalid expiration date
    Given JS library is configured with BYPASS_CARDS_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MAESTRO_CARD
    And User clicks Pay button
    Then User will see payment status information: "Maestro must use SecureCode"
    And User will see that notification frame has "red" color

  @reactJS
  @angular
  Scenario: Successful payment with frictionless card
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @reactJS
  @angular
  Scenario: Successful payment with non-frictionless card
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @reactJS
  @angular
  Scenario: Successful payment after form validation
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    When User clicks Pay button
    And User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color