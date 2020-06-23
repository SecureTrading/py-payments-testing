Feature: ApplePay
  As a user
  I want to use ApplePay payment method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @full_test_part_1 @wallet_test @apple_test
  Scenario Outline: ApplePay - checking payment status for <action_code> response code
    When User chooses ApplePay as payment method - response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And APPLE_PAY or AUTH requests were sent only once with correct data
    @smoke_test_part_1
    Examples:
      | action_code | payment_status_message                  | color |
      | SUCCESS     | Payment has been successfully processed | green |
    Examples:
      | action_code | payment_status_message     | color  |
#      | ERROR       | "Invalid response"          | red    |
      | DECLINE     | Decline                    | red    |
      | CANCEL      | Payment has been cancelled | yellow |

  @base_config @full_test_part_2 @translations @apple_test
  Scenario Outline: ApplePay - checking translation for "Payment has been cancelled" status for <language>
    When User changes page language to "<language>"
    When User chooses ApplePay as payment method - response is set to "CANCEL"
    Then User will see "Payment has been cancelled" payment status translated into "<language>"
    Examples:
      | language |
      | es_ES    |
#      | no_NO    |

  @config_submit_on_success_true @smoke_test_part_1 @full_test_part_2 @apple_test
  Scenario: ApplePay - successful payment with enabled 'submit on success' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User chooses ApplePay as payment method - response is set to "SUCCESS"
    Then User is redirected to action page

  @config_default @smoke_test_part_1 @full_test_part_2 @apple_test
  Scenario: ApplePay - checking that 'submitOnSuccess' is enabled by default
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User chooses ApplePay as payment method - response is set to "SUCCESS"
        Then User is redirected to action page

  @config_submit_on_error_true @full_test_part_2 @apple_test
  Scenario: ApplePay - error payment with enabled 'submit on error' process
    When User chooses ApplePay as payment method - response is set to "DECLINE"
    Then User is redirected to action page

  @config_submit_on_cancel_true @smoke_test_part_2 @full_test_part_2 @apple_test
  Scenario: ApplePay - canceled payment with enabled 'submit on cancel' process
    When User chooses ApplePay as payment method - response is set to "CANCEL"
    Then User is redirected to action page

  @base_config @full_test_part_1 @wallet_test @apple_test
  Scenario Outline: ApplePay - checking <callback> callback functionality
    When User chooses ApplePay as payment method - response is set to "<action_code>"
    Then User will see "<callback>" popup
    @smoke_test_part_1
    Examples:
      | action_code | callback |
      | SUCCESS     | success  |
    Examples:
      | action_code | callback |
      | DECLINE     | error    |
      | CANCEL      | cancel   |

  @config_update_jwt_true @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - Successful payment with updated JWT
    When User fills amount field
    When User chooses ApplePay as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And APPLE_PAY or AUTH requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_apple_auth @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - successful payment with additional request types: ACCOUNTCHECK, AUTH
    When AUTH ApplePay mock response is set to SUCCESS
    And User chooses ApplePay as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH request for APPLE_PAY is sent only once with correct data

  @config_apple_acheck @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - successful payment with additional request types: ACCOUNTCHECK
    When ACCOUNTCHECK ApplePay mock response is set to SUCCESS
    And User chooses ApplePay as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And ACCOUNTCHECK request for APPLE_PAY is sent only once with correct data

  @config_apple_acheck_auth @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - successful payment with additional request types: ACCOUNTCHECK, AUTH
    When ACCOUNTCHECK, AUTH ApplePay mock response is set to SUCCESS
    And User chooses ApplePay as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And ACCOUNTCHECK, AUTH request for APPLE_PAY is sent only once with correct data

  @config_apple_riskdec_auth @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - successful payment with additional request types: ACCOUNTCHECK, AUTH
    When RISKDEC, AUTH ApplePay mock response is set to SUCCESS
    And User chooses ApplePay as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And RISKDEC, AUTH request for APPLE_PAY is sent only once with correct data

  @config_apple_riskdec_acheck_auth @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - successful payment with additional request types: ACCOUNTCHECK, AUTH
    When RISKDEC, ACCOUNTCHECK, AUTH ApplePay mock response is set to SUCCESS
    And User chooses ApplePay as payment method
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And RISKDEC, ACCOUNTCHECK, AUTH request for APPLE_PAY is sent only once with correct data

  @config_cybertonica @smoke_test_part_2 @full_test_part_2
  Scenario: ApplePay - Cybertonica - 'fraudcontroltransactionid' flag is added to AUTH requests during payment
    When User chooses ApplePay as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag

  @base_config @full_test_part_2 @cybertonica
  Scenario: ApplePay - Cybertonica - 'fraudcontroltransactionid' flag is not added to AUTH requests during payment
    When User chooses ApplePay as payment method - response is set to "SUCCESS"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH request was sent only once without 'fraudcontroltransactionid' flag

#  @base_config @parent_iframe @full_test_part_2 @full_test
#  Scenario: ApplePay - successful payment when app is embedded in another iframe
#    When User opens payment page
#    When User chooses ApplePay as payment method - response is set to "SUCCESS"
#    Then User will see payment status information: "Payment has been successfully processed"
#    And User will see that notification frame has "green" color
#    And APPLE_PAY or AUTH requests were sent only once with correct data
#
#  @configApplePayRiskdecAcheckAuth @full_test_part_2 @full_test
#  Scenario: ApplePay - successful payment when app is embedded in another iframe
#    When User opens payment page
#    When User chooses ApplePay as payment method - response is set to "SUCCESS"
#    Then User will see payment status information: "Payment has been successfully processed"
#    And User will see that notification frame has "green" color
#    And APPLE_PAY or AUTH requests were sent only once with correct data