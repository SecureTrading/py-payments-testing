Feature: E2E startOnLoad

  As a user
  I want to use card payments method with startOnLoad config
  In order to check full payment functionality


  Scenario: Successful non-frictionless payment with startOnLoad
    Given JS library is configured with START_ON_LOAD_CONFIG and JWT_WITH_NON_FRICTIONLESS_CARD
    And User opens example page WITHOUT_SUBMIT_BUTTON
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  Scenario: Successful payment with startOnLoad and additional request types: ACCOUNTCHECK, TDQ, AUTH
    Given JS library is configured with START_ON_LOAD_REQUEST_TYPES_CONFIG and JWT_WITH_FRICTIONLESS_CARD
    And User opens example page WITHOUT_SUBMIT_BUTTON
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

    Scenario: Successful payment with startOnLoad and additional request types: ACCOUNTCHECK, TDQ, AUTH, SUBSCRIPTION
    Given JS library is configured with START_ON_LOAD_REQUEST_TYPES_SUB_CONFIG and JWT_NON_FRICTIONLESS_CARD_SUBSCRIPTION
    And User opens example page WITHOUT_SUBMIT_BUTTON
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
