Feature: Immediate payment

  As a user
  I want to use card payments method with immediate config
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_immediate_payment_tdq
  Scenario: Immediate payment - Successful payment with request types: THREEDQUERY
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data

  @config_immediate_payment_acheck_tdq_auth_riskdec
  Scenario: Immediate payment - Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH, RISKDEC
    When ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And ACS mock response is set to "OK"
    And AUTH, RISKDEC mock response is set to OK
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    #ToDo - check this step
    #And AUTH, RISKDEC ware sent only once in one request

  @config_immediate_payment_tdq_auth
  Scenario: Immediate payment - Successful payment with request types: THREEDQUERY, AUTH
    When ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_immediate_payment_acheck_tdq_auth
  Scenario: Immediate payment - Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH
    When ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_immediate_payment_riskdec_acheck_tdq_auth
  Scenario: Immediate payment - Successful payment with additional request types: RISKDEC, ACCOUNTCHECK, THREEDQUERY, AUTH
    When RISKDEC, ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_immediate_payment
  Scenario: Immediate payment (card enrolled N) - checking payment status for OK response code
    When THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And JSINIT request was sent only 1
    And AUTH and THREEDQUERY requests were sent only once

  @config_immediate_payment
  Scenario: Immediate payment (card enrolled Y) - check ACS response for code: FAILURE
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "FAILURE"
    And User opens payment page
    Then User will see payment status information: "An error occurred"
    And THREEDQUERY request was sent only once with correct data

  @config_immediate_payment_and_submit_on_success @smoke_test @extended_tests_part_1
  Scenario: Immediate payment with submitOnSuccess - successful payment
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once

  @config_immediate_payment_and_defer_init
  Scenario: Immediate payment with deferInit - successful payment
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And JSINIT request was sent only 1
    And AUTH and THREEDQUERY requests were sent only once

  @config_immediate_payment @extended_tests_part_1
  Scenario Outline: Immediate payment (card enrolled Y) - checking payment status for <action_code> response code
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "<action_code>"
    And User opens payment page
    Then User will see payment status information: "<payment_status_message>"
    And AUTH and THREEDQUERY requests were sent only once

    @smoke_test
    Examples:
      | action_code | payment_status_message                  |
      | OK          | Payment has been successfully processed |

    Examples:
      | action_code | payment_status_message |
      | DECLINE     | Decline                |