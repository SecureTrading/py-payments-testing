Feature: Successfull payments with various request types configurations

  As a user
  I want to use card payments method with request types configurations
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_requestTypes_tdq
  Scenario: Successful payment with request types: THREEDQUERY
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data

  @config_requestTypes_tdq_auth
  Scenario: Successful payment with request types: THREEDQUERY, AUTH
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_requestTypes_acheck_tdq_auth
  Scenario: Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_requestTypes_tdq_auth_riskdec
  Scenario: Successful payment with additional request types: THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data
    And AUTH, RISKDEC ware sent only once in one request

  @config_requestTypes_riskdec_acheck_tdq_auth
  Scenario: Successful payment with additional request types: RISKDEC, ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_requestTypes_acheck_tdq_auth_riskdec
  Scenario: Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH, RISKDEC ware sent only once in one request

  @config_requestTypes_tdq_submit_on_success
  Scenario: Successful payment with request types: THREEDQUERY and submitOnSuccess
    Given User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    When User fills payment form with defined card VISA_CARD
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button
    Then User is redirected to action page
    And THREEDQUERY request was sent only once with correct data

  @config_requestTypes_acheck_tdq_auth_subs
  Scenario: Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH, SUBSCRIPTION
    JWT_WITH_SUBSCRIPTION
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH, RISKDEC ware sent only once in one request

  @config_requestTypes_tdq_acheck_riskdec_auth
  Scenario: Successful payment with additional request types: THREEDQUERY, ACCOUNTCHECK, RISKDEC, AUTH
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH, RISKDEC ware sent only once in one request