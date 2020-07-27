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

  @e2e_config_submit_on_success
  Scenario: Successful payment with submitOnSuccess enabled
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |
