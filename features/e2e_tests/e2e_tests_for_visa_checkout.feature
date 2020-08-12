Feature: Visa checkout E2E tests
  As a user
  I want to use visa checkout
  To use defined card

  #ToDo - Work in progress
  #change email and add one time code reader from email
  Background:
#    ToDo - Uncomment this line when environment for e2e test will be ready
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
    Given User opens page with payment form

  @base_config
  Scenario: Successful Authentication by Visa checkout
    When User clicks on Visa Checkout button
    And User fills visa checkout email address
    And User fills visa checkout one time password
    And User confirm displayed card with data
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"