Feature: Successfull payments with start on load configuration

  As a user
  I want to use start on load option when submit button is not displayed
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    
  @config_start_on_load_requestTypes_tdq
  Scenario: Successful payment with startOnLoad and request types THREEDQUERY
    When THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And AUTH response is set to "OK"
    And User opens prepared payment form page WITHOUT_SUBMIT_BUTTON
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY ware sent only once in one request

  @config_start_on_load_sub_acheck_tdq_aut
  Scenario: Successful payment with startOnLoad and request types ACCOUNTCHECK, THREEDQUERY, AUTH, SUBSCRIPTION
    When ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And ACS mock response is set to "OK"
    And AUTH, SUBSCRIPTION mock response is set to OK
    And User opens prepared payment form page WITHOUT_SUBMIT_BUTTON
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request

  @config_start_on_load_requestTypes_tdq_auth
  Scenario: Successful payment with startOnLoad request types: THREEDQUERY, AUTH
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens prepared payment form page WITHOUT_SUBMIT_BUTTON
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data