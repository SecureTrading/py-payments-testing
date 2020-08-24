Feature: E2E for form id

  As a user
  I want to use card payments method with another formId
  In order to check full payment functionality

  Background:
    Given JS library is configured with CHANGED_FORM_ID_CONFIG and BASE_JWT
    And User opens example page WITH_CHANGED_FORM_ID

  Scenario: Successful non-frictionless payment with form id
    When User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  Scenario: Successful frictionless payment with form id
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"