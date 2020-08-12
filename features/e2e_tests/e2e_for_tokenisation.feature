Feature: E2E for tokenisation
  As a user
  I want to use predefined jwt config files
  To execute payment with only cvv

  Background:
#    ToDo - Uncomment this line when environment for e2e test will be ready
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
    Given User opens page with payment form

  @e2e_for_tokenisation @jwt_config_visa_frictionless_with_parenttransaction
  Scenario: Visa Frictionless tokenisation
    When User fills only security code for saved VISA_FRICTIONLESS card
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"

  @e2e_for_tokenisation @jwt_config_visa_non_frictionless_with_parenttransaction
  Scenario: Visa Non-Frictionless tokenisation
    When User fills only security code for saved VISA_NON_FRICTIONLESS card
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"

  @e2e_for_tokenisation @jwt_config_amex_non_frictionless_with_parenttransaction
  Scenario: Amex Non-Frictionless tokenisation
    When User fills only security code for saved AMEX_NON_FRICTIONLESS card
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"
    