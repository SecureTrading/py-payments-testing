Feature: E2E tests for iframe
  As a user
  I want to use iframe page
  To make payment

  Background:
#    ToDo - Uncomment this line when environment for e2e test will be ready
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
    Given User opens payment page

  @e2e_config_for_iframe @parent_iframe
  Scenario: Successful frictionless payment on iframe
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @e2e_config_for_iframe_start_on_load_true @parent_iframe @jwt_config_start_on_load_true
  Scenario: Successful non-frictionless payment on iframe
    When User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"