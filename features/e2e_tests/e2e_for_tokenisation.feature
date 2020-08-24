Feature: E2E for tokenisation
  As a user
  I want to use predefined jwt config files
  To execute payment with only cvv

  @reactJS
  @e2e_for_tokenisation @jwt_config_visa_frictionless_with_parenttransaction
  Scenario: Visa Frictionless tokenisation
    Given JS library is configured with TOKENISATION_CONFIG and JWT_VISA_FRICTIONLESS_PARENT_TRANSACTION
    And User opens example page
    When User fills only security code for saved VISA_FRICTIONLESS card
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"

  @e2e_for_tokenisation @jwt_config_visa_non_frictionless_with_parenttransaction
  Scenario: Visa Non-Frictionless tokenisation
    Given JS library is configured with TOKENISATION_CONFIG and JWT_VISA_NON_FRICTIONLESS_PARENT_TRANSACTION
    And User opens example page
    When User fills only security code for saved VISA_NON_FRICTIONLESS card
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"

  @e2e_for_tokenisation @jwt_config_amex_non_frictionless_with_parenttransaction
  Scenario: Amex Non-Frictionless tokenisation
    Given JS library is configured with TOKENISATION_CONFIG and JWT_AMEX_NON_FRICTIONLESS_PARENT_TRANSACTION
    And User opens example page
    When User fills only security code for saved AMEX_NON_FRICTIONLESS card
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that SECURITY_CODE input fields are "disabled"
    