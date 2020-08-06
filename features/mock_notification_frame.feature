Feature: Notification frame

  As a user
  I want to use card payments method
  In order to check notification frame after payment

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_disable_notifications_true @extended_tests_part_1
  Scenario: Notification frame is not displayed after payment
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will not see notification frame

  @config_submit_on_success_and_error_true
  Scenario Outline: Notification frame is not displayed after payment with submitOn<submitOn>
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will not see notification frame

    Examples:
      | submitOn | action_code |
      | Success  | OK          |
      | Error    | DECLINE     |

  @base_config
  Scenario: Checking notification banner style after second payment
    When User fills payment form with credit card number "5100000000000412", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_U"
    And User clicks Pay button - AUTH response is set to "UNAUTHENTICATED"
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color
    When User fills payment form with credit card number "5100000000000412", expiration date "01/22" and cvv "123"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color