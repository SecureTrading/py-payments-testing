Feature: Callback functionality

  As a user
  I want to use card payments method
  In order to check callback popup in payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @extended_tests_part_2
  Scenario Outline: Checking <action_code> callback functionality
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see "<callback_popup>" popup
    And "<callback_popup>" callback is called only once

    @smoke_test
    Examples:
      | action_code | callback_popup |
      | OK          | success        |

    Examples:
      | action_code | callback_popup |
      | DECLINE     | error          |

  @base_config
  Scenario: Checking callback function for in-browser validation
    When User clicks Pay button
    Then User will see "error" popup
    And "error" callback is called only once

  @base_config
  Scenario: Checking data type passing to callback function
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see correct error code displayed in popup
    And "submit" callback is called only once