Feature: Cardinal commerce

  As a user
  I want to use card payments method with cardinal commerce config
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @cardinal_commerce
  Scenario Outline: Cardinal Commerce (step-up payment) - checking payment status for <action_code> response code
    When User fills payment form with credit card number "<card_number>", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

    @smoke_test @extended_tests_part_1
    Examples:
      | card_number      | action_code | payment_status_message                  | color |
      | 4000000000001091 | OK          | Payment has been successfully processed | green |
      | 4000000000001109 | DECLINE     | Decline                                 | red   |
    Examples:
      | card_number      | action_code     | payment_status_message | color |
      #|4000000000001109 | INVALID_FIELD   | Invalid field        | red   |
      | 4000000000001109 | SOCKET_ERROR    | Socket receive error   | red   |
      | 4000000000001109 | UNAUTHENTICATED | Unauthenticated        | red   |
      #|4000000000001109 | UNKNOWN_ERROR   | Unknown error        | red   |

  @base_config @cardinal_commerce
  Scenario Outline: Cardinal Commerce (frictionless cards) - checking payment status for <action_code> response code
    When User fills payment form with credit card number "<card_number>", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

    @extended_tests_part_1
    Examples:
      | card_number      | action_code | payment_status_message                  | color |
      | 4000000000001026 | OK          | Payment has been successfully processed | green |
    Examples:
      | card_number      | action_code     | payment_status_message | color |
      | 4000000000001018 | UNAUTHENTICATED | Unauthenticated        | red   |
      | 4000000000001018 | DECLINE         | Decline                | red   |

  @base_config @cardinal_commerce
  Scenario Outline: Cardinal Commerce (card not-enrolled U) - checking payment status for <action_code> response code
    When User fills payment form with credit card number "<card_number>", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_U"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

    Examples:
      | card_number      | action_code     | payment_status_message                  | color |
      | 4111110000000401 | OK              | Payment has been successfully processed | green |
      | 5100000000000412 | UNAUTHENTICATED | Unauthenticated                         | red   |
      #|5100000000000412	 | DECLINE         | Decline                | red   |

  @base_config @extended_tests_part_1
  Scenario: Cardinal Commerce - check THREEDQUERY response for code: "INVALID_ACQUIRER"
    When User fills payment form with credit card number "4111110000000211", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "INVALID_ACQUIRER"
    And User clicks Pay button
    Then User will see payment status information: "Invalid acquirer for 3-D Secure"
    And User will see that notification frame has "red" color
    And THREEDQUERY request was sent only once with correct data

  @base_config @extended_tests_part_1
  Scenario: Cardinal Commerce - check ACS response for code: FAILURE
    When User fills payment form with credit card number "4111110000000211", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "FAILURE"
    And User clicks Pay button
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color
    And THREEDQUERY request was sent only once with correct data
    And User will see that Submit button is "enabled" after payment

  @base_config @cardinal_commerce
  Scenario Outline: Cardinal Commerce - check ACS response for code: <action_code>
    When User fills payment form with credit card number "4111110000000211", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "<action_code>"
    And User clicks Pay button
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

    Examples:
      | action_code | payment_status_message                  | color |
      | NOACTION    | Payment has been successfully processed | green |

