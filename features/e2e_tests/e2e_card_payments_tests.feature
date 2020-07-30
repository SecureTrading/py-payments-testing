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
  Scenario Outline: Successful payment bypass cards without 3d secure
    When User fills payment form with defined card <card>
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

    Examples:
      | card                    |
      | VISA_STEP_UP_CARD       |
      | MASTERCARD_STEP_UP_CARD |
