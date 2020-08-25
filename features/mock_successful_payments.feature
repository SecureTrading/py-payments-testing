Feature: Successfull payments with various configurations

  As a user
  I want to use card payments method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag

  @base_config @extended_tests_part_1 @cardinal_commerce
  Scenario Outline: Successful payment using most popular Credit Cards: <card_type>
    Given User opens page with payment form
    When User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>" and cvv "<cvv>"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once with correct data

    @smoke_test
    Examples:
      | card_number      | expiration_date | cvv | card_type |
      | 4111110000000211 | 12/22           | 123 | VISA      |

    Examples:
      | card_number      | expiration_date | cvv  | card_type  |
      | 5100000000000511 | 12/22           | 123  | MASTERCARD |
      | 340000000000611  | 12/22           | 1234 | AMEX       |

  @config_update_jwt_true @smoke_test @extended_tests_part_2
  Scenario: Successful payment with updated JWT
    Given User opens prepared payment form page WITH_UPDATE_JWT
      | jwtName          |
      | BASE_UPDATED_JWT |
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And User calls updateJWT function by filling amount field
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_defer_init
  Scenario: Successful payment with deferInit
    Given User opens page with payment form
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And JSINIT request was not sent
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    Then JSINIT request was sent only 1
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_defer_init
  Scenario: Successful payment with deferInit and updated JWT
    Given User opens prepared payment form page WITH_UPDATE_JWT
      | jwtName          |
      | BASE_UPDATED_JWT |
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And User calls updateJWT function by filling amount field
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_submit_cvv_only @extended_tests_part_2
  Scenario: Successful payment when cvv field is selected to submit
    Given User opens page with payment form
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will not see CARD_NUMBER
    And User will not see EXPIRATION_DATE
    And AUTH and THREEDQUERY requests were sent only once

  @config_submit_cvv_for_amex
  Scenario: Successful payment by AMEX when cvv field is selected to submit
    Given User opens page with payment form
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will not see CARD_NUMBER
    And User will not see EXPIRATION_DATE
    And AUTH and THREEDQUERY requests were sent only once

  @config_cvvToSubmit_and_submitOnSuccess
  Scenario: Successful payment with fieldToSubmit and submitOnSuccess
    Given User opens page with payment form
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once

  @config_skip_jsinit @cardinal_commerce
  Scenario: Successful payment with skipped JSINIT process
    Given User opens page with payment form
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @base_config
  Scenario: Submit payment form by 'Enter' button
    Given User opens page with payment form
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User press enter button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see the same provided data in inputs fields