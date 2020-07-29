Feature: Card Payments

  As a user
  I want to use card payments method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @extended_tests_part_1
  Scenario Outline: Payment form accessibility after payment process
    When User fills payment form with credit card number "4000000000001000", expiration date "12/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see that Submit button is "<form_status>" after payment
    And User will see that all input fields are "<form_status>"

    @smoke_test
    Examples:
      | action_code | form_status |
      | OK          | disabled    |

    Examples:
      | action_code | form_status |
      | DECLINE     | enabled     |

  @config_default
  Scenario: Checking that 'submitOnSuccess' is enabled by default
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_requestTypes_tdq_submit_on_error
  Scenario: Error payment with request types: THREEDQUERY and submitOnError
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "INVALID_ACQUIRER"
    And User clicks Pay button
    Then User is redirected to action page
    And THREEDQUERY request was sent only once with correct data

  @config_incorrect_request_type @extended_tests_part_2
  Scenario: Checking request types validation
    When User sets incorrect request type in config file
    Then User will see that application is not fully loaded

  @base_config
  Scenario: Verify number on JSINIT requests
    Then JSINIT request was sent only 1

  @base_config
  Scenario: Verify number of JSINIT requests together with UpdateJWT
    When User fills amount field
    And User fills amount field
    Then JSINIT request was sent only 2
    And JSINIT requests contains updated jwt

  @base_config
  Scenario: Security code re-enabled if server error on PIBA
    When User fills payment form with credit card number "3089500000000000021", expiration date "12/23"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "DECLINE"
    Then User will see payment status information: "Decline"
    And User will see that "SECURITY_CODE" field is disabled