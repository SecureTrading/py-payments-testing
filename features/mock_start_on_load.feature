Feature: Successfull payments with start on load configuration

  As a user
  I want to use start on load option
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_requestTypes_tdq_start_on_load
  Scenario: Successful payment with request types THREEDQUERY and start on load
    When THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data

  @config_requestTypes_tdq_auth_start_on_load
  Scenario: Successful payment with request types: THREEDQUERY, AUTH
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once with correct data