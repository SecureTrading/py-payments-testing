Feature: Visa Checkout
 As a user
  I want to use Visa Checkout payment method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @extended_tests_part_2 @wallet_test @visa_test
  Scenario Outline: Visa Checkout - checking payment status for <action_code> response code
    When User chooses Visa Checkout as payment method - response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data
    @smoke_test
    Examples:
      | action_code | payment_status_message                  | color |
      | SUCCESS     | Payment has been successfully processed | green |
    Examples:
      | action_code | payment_status_message     | color  |
      | CANCEL      | Payment has been cancelled | yellow |
      | ERROR       | Wystąpił błąd              | red    |

  @config_submit_on_success_true @extended_tests_part_2 @visa_test
  Scenario: Visa Checkout - successful payment with enabled 'submit on success' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User is redirected to action page

  @config_submit_on_error_true @visa_test
  Scenario: Visa Checkout - error payment with enabled 'submit on error' process
    When User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User is redirected to action page

  @config_submit_on_cancel_true @visa_test
  Scenario: Visa Checkout - canceled payment with enabled 'submit on cancel' process
    When User chooses Visa Checkout as payment method - response is set to "CANCEL"
    Then User is redirected to action page

  @base_config @wallet_test
  Scenario Outline: Visa Checkout - checking <callback> callback functionality
    When User chooses Visa Checkout as payment method - response is set to "<action_code>"
    Then User will see "<callback>" popup
    @extended_tests_part_2
    Examples:
      | action_code | callback |
      | SUCCESS     | success  |
    Examples:
      | action_code | callback |
      | ERROR       | error    |
      | CANCEL      | cancel   |

  @config_update_jwt_true @extended_tests_part_2
  Scenario: Visa Checkout - successful payment with updated JWT
    When User fills amount field
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_cybertonica
  Scenario: Visa Checkout - Cybertonica - 'fraudcontroltransactionid' flag is added to AUTH requests during payment
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag

  @base_config @cybertonica
  Scenario: Visa Checkout - Cybertonica - 'fraudcontroltransactionid' flag is not added to AUTH requests during payment
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once without 'fraudcontroltransactionid' flag

  @base_config @parent_iframe @full_test
  Scenario: Visa Checkout - successful payment when app is embedded in another iframe
    When User opens payment page
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @base_config @visa_test @translations
  Scenario Outline: Visa Checkout - check translation overwriting mechanism
    When User changes page language to "<language>"
    And User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User will see notification frame with message: "Wystąpił błąd"
    And User will see that notification frame has "red" color
    Examples:
      | language |
      | fr_FR    |
