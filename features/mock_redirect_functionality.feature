Feature: Redirect functionality

  As a user
  I want to use card payments method with redirect config
  In order to check if user is redirected or not after submit form action with success or error result

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_default
  Scenario: Cardinal Commerce - successful payment - checking that 'submitOnSuccess' is enabled by default
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_requestTypes_tdq_submit_on_error
  Scenario: Error payment with request types: THREEDQUERY and submitOnError
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "INVALID_ACQUIRER"
    And User clicks Pay button
    Then User is redirected to action page
    And THREEDQUERY request was sent only once with correct data

  @config_submit_on_error_true @smoke_test @extended_tests_part_1
  Scenario: Cardinal Commerce - error payment with enabled 'submit on error' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "DECLINE"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_submit_on_error_false
  Scenario: Cardinal Commerce - error payment with disabled 'submit on error' process
    When User fills payment form with defined card MASTERCARD_NOT_ENROLLED_CARD
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "DECLINE"
    Then User remains on checkout page
    And User will see payment status information: "Decline"
    And User will see that notification frame has "red" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_submit_on_success_true @smoke_test @extended_tests_part_1
  Scenario: Cardinal Commerce - successful payment with enabled 'submit on success' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    And User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data