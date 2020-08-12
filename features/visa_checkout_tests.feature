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
      | ERROR       | An error occurred          | red    |

  @config_submit_on_success_true @extended_tests_part_2 @visa_test
  Scenario: Visa Checkout - successful payment with enabled 'submitOnSuccess' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User is redirected to action page

  @config_default @visa_test
  Scenario: Visa Checkout - successful payment - checking that 'submitOnSuccess' is enabled by default
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User is redirected to action page
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @config_submit_on_error_true @visa_test
  Scenario: Visa Checkout - error payment with enabled 'submitOnError' process
    When User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User is redirected to action page

  @config_submit_on_success_error_cancel_false @visa_test
  Scenario: Visa Checkout - error payment with disabled 'submitOnError' process
    When User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User remains on checkout page
    And User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @config_default @visa_test
  Scenario: Visa Checkout - error payment - checking that 'submitOnError' is disabled by default
    When User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User remains on checkout page
    And User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @config_submit_on_cancel_true @visa_test
  Scenario: Visa Checkout - canceled payment with enabled 'submitOnCancel' process
    When User chooses Visa Checkout as payment method - response is set to "CANCEL"
    Then User is redirected to action page

  @config_submit_on_success_error_cancel_false @visa_test
  Scenario: Visa Checkout - canceled payment with disabled 'submitOnCancel' process
    When User chooses Visa Checkout as payment method - response is set to "CANCEL"
    Then User remains on checkout page
    And User will see payment status information: "Payment has been cancelled"
    And User will see that notification frame has "yellow" color

  @config_default @visa_test
  Scenario: Visa Checkout - canceled payment - checking that 'submitOnCancel' is disabled by default
    When User chooses Visa Checkout as payment method - response is set to "CANCEL"
    Then User remains on checkout page
    And User will see payment status information: "Payment has been cancelled"
    And User will see that notification frame has "yellow" color

  @base_config @wallet_test @visa_test
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


  @config_update_jwt_true @extended_tests_part_2 @visa_test
  Scenario: Visa Checkout - successful payment with updated JWT
    When User calls updateJWT function by filling amount field
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data
    And VISA_CHECKOUT requests contains updated jwt

  @config_defer_init @smoke_test @visa_test
  Scenario: Visa Checkout - Successful payment with deferInit and updated JWT
    When User calls updateJWT function by filling amount field
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data
    And VISA_CHECKOUT requests contains updated jwt

  @config_submit_on_success_true @smoke_test @visa_test
  Scenario: Visa Checkout - with submitOnSuccess and updated JWT
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User calls updateJWT function by filling amount field
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User is redirected to action page
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data
    And VISA_CHECKOUT requests contains updated jwt

  @config_cybertonica @visa_test
  Scenario: Visa Checkout - Cybertonica - 'fraudcontroltransactionid' flag is added to AUTH requests during payment
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag

  @base_config @cybertonica @visa_test
  Scenario: Visa Checkout - Cybertonica - 'fraudcontroltransactionid' flag is not added to AUTH requests during payment
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once without 'fraudcontroltransactionid' flag

  @base_config @parent_iframe @full_test @visa_test
  Scenario: Visa Checkout - successful payment when app is embedded in another iframe
    When User opens payment page
    And User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @config_translations @visa_test @translations
  Scenario Outline: Visa Checkout - check translation overwriting mechanism
    When User changes page language to "<language>"
    And User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User will see notification frame with message: "Wystąpił błąd"
    And User will see that notification frame has "red" color
    Examples:
      | language |
      | fr_FR    |

  @config_disable_notifications_true @visa_test
  Scenario: Visa Checkout - notification frame is not displayed after successful payment
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will not see notification frame

  @config_disable_notifications_true @visa_test
  Scenario: Visa Checkout - notification frame is not displayed after declined payment
    When User chooses Visa Checkout as payment method - response is set to "ERROR"
    Then User will not see notification frame

  @config_disable_notifications_false @visa_test
  Scenario: Visa Checkout - notification frame is displayed after payment if disableNotification is false
    When User chooses Visa Checkout as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @config_visa_auth @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: AUTH
    When AUTH Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_acheck_auth @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: ACCOUNTCHECK, AUTH
    When ACCOUNTCHECK, AUTH Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And ACCOUNTCHECK, AUTH request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_acheck @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: ACCOUNTCHECK
    When ACCOUNTCHECK Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And ACCOUNTCHECK request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_riskdec_auth @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: RISKDEC, AUTH
    When RISKDEC, AUTH Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And RISKDEC, AUTH request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_riskdec_acheck_auth @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: RISKDEC, ACCOUNTCHECK, AUTH
    When RISKDEC, ACCOUNTCHECK, AUTH Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And RISKDEC, ACCOUNTCHECK, AUTH request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_auth_subscription @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: AUTH, SUBSCRIPTION
    When AUTH, SUBSCRIPTION Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH, SUBSCRIPTION request for VISA_CHECKOUT is sent only once with correct data

  @config_visa_acheck_subscription @visa_test
  Scenario: Visa Checkout - successful payment with additional request types: ACCOUNTCHECK, SUBSCRIPTION
    When ACCOUNTCHECK, SUBSCRIPTION Visa Checkout mock response is set to SUCCESS
    And User chooses VISA_CHECKOUT as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And ACCOUNTCHECK, SUBSCRIPTION request for VISA_CHECKOUT is sent only once with correct data
