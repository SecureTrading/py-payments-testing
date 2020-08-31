Feature: Card Payments

  As a user
  I want to use card payments method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag

  @base_config @extended_tests_part_1
  Scenario Outline: Payment form accessibility after payment process
    Given User opens page with payment form
    When User fills payment form with credit card number "4000000000001000", expiration date "12/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see that Submit button is "<form_status>" after payment
    And User will see that ALL input fields are "<form_status>"

    @smoke_test
    Examples:
      | action_code | form_status |
      | OK          | disabled    |

    Examples:
      | action_code | form_status |
      | DECLINE     | enabled     |

  @config_incorrect_request_type @extended_tests_part_2
  Scenario: Checking request types validation
    Given User opens page with payment form
    When User sets incorrect request type in config file
    Then User will see that application is not fully loaded

  @base_config
  Scenario: Verify number on JSINIT requests
    When User opens page with payment form
    Then JSINIT request was sent only 1

  @base_config
  Scenario: Verify number of JSINIT requests together with UpdateJWT
    Given User opens prepared payment form page WITH_UPDATE_JWT
      | jwtName          |
      | BASE_UPDATED_JWT |
    When User calls updateJWT function by filling amount field
    And User calls updateJWT function by filling amount field
    Then JSINIT request was sent only 2
    And JSINIT requests contains updated jwt

  @base_config
  Scenario: Security code re-enabled if server error on PIBA
    Given User opens page with payment form
    When User fills payment form with credit card number "3089500000000000021", expiration date "12/23"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "DECLINE"
    Then User will see payment status information: "Decline"
    And User will see that "SECURITY_CODE" field is disabled