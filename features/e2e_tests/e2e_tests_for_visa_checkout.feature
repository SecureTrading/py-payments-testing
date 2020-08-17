Feature: Visa checkout E2E tests

  As a user
  I want to use visa checkout
  To use defined card

  Background:
#    ToDo - Uncomment this line when environment for e2e test will be ready
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
    Given User opens page with payment form

  @base_config
  Scenario Outline: Successful Authentication by Visa checkout
    Given User clicks on Visa Checkout button
    And User fills visa checkout email address
    And User fills visa checkout one time password
    When User select <visa_card_type> card on visa checkout popup
    And User confirm displayed card with data
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

    Examples:
      | visa_card_type        |
      | VISA_FRICTIONLESS     |
      | VISA_NON_FRICTIONLESS |

  @base_config
  Scenario: Declined Authentication by Visa checkout using declined visa card
    Given User clicks on Visa Checkout button
    And User fills visa checkout email address
    And User fills visa checkout one time password
    When User select VISA_DECLINED_CARD card on visa checkout popup
    And User confirm displayed card with data
    Then User will see payment status information: "Decline"
    And User will see that notification frame has "red" color