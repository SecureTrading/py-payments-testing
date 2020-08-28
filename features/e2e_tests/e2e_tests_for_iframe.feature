Feature: E2E tests for iframe
  As a user
  I want to use iframe page
  To make payment

  @reactJS
  @angular
  @e2e_config_for_iframe @parent_iframe
  Scenario: Successful frictionless payment on iframe
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page IN_IFRAME
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @e2e_config_for_iframe_start_on_load_true @parent_iframe @jwt_config_start_on_load_true
  Scenario: Successful non-frictionless payment with startOnLoad on iframe
    Given JS library is configured with START_ON_LOAD_CONFIG and JWT_WITH_NON_FRICTIONLESS_CARD
    And User opens example page IN_IFRAME
    When User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"