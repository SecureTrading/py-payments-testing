Feature: E2E Card Payments
  As a user
  I want to use card payments method
  In order to check full payment functionality

  Background:
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
#    And JWT token is prepared
    Given User opens page with payment form

  @e2e_config_bypass_mastercard
  Scenario: Successful payment with bypassCard using Mastercard
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_for_bypass_cards
  Scenario: Successful payment bypass cards without 3d secure
    When User fills payment form with defined card VISA_STEP_UP_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_for_bypass_cards
  Scenario: Successful payment bypass cards with 3d secure
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_AUTH_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_bypass_mastercard
  Scenario: Unsuccessful payment with bypassCard using Mastercard - invalid expiration date
    When User fills payment form with defined card MASTERCARD_INVALID_EXP_DATE_CARD
    And User clicks Pay button
    Then User will see payment status information: "Invalid field"
    And User will see that notification frame has "red" color
    And User will see that "EXPIRATION_DATE" field is highlighted
    And User will see "Invalid field" message under field: "EXPIRATION_DATE"
