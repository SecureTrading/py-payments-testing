Feature: Card Payments
  As a user
  I want to use card payments method
  In order to check full payment functionality

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @extended_tests_part_1 @cardinal_commerce
  Scenario Outline: Cardinal Commerce (step-up payment) - checking payment status for <action_code> response code
    When User fills payment form with credit card number "<card_number>", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    @smoke_test
    Examples:
      | card_number      | action_code | payment_status_message                  | color |
      | 4000000000001091 | OK          | Payment has been successfully processed | green |
      | 4000000000001109 | DECLINE     | Decline                                 | red   |
    Examples:
      | card_number      | action_code     | payment_status_message | color |
#     |4000000000001109 | INVALID_FIELD   | Invalid field        | red   |
      | 4000000000001109 | SOCKET_ERROR    | Socket receive error   | red   |
      | 4000000000001109 | UNAUTHENTICATED | Unauthenticated        | red   |
#     |4000000000001109 | UNKNOWN_ERROR   | Unknown error        | red   |

  @base_config @extended_tests_part_1 @cardinal_commerce
  Scenario Outline: Cardinal Commerce (frictionless cards) - checking payment status for <action_code> response code
    When User fills payment form with credit card number "<card_number>", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    Examples:
      | card_number      | action_code     | payment_status_message | color |
      | 4000000000001018 | UNAUTHENTICATED | Unauthenticated        | red   |
      | 4000000000001026 | OK          | Payment has been successfully processed | green |
      | 4000000000001018 | DECLINE     | Decline                                 | red   |

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
#     |5100000000000412	 | DECLINE         | Decline                | red   |

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
    Then User will see payment status information: "Wystąpił błąd"
    And User will see that notification frame has "red" color
    And THREEDQUERY request was sent only once with correct data
    And User will see that Submit button is "enabled" after payment

  @base_config @extended_tests_part_1 @cardinal_commerce
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

  @base_config @extended_tests_part_1 @cardinal_commerce
  Scenario Outline: Successful payment using most popular Credit Cards: <card_type>
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

  @config_animated_card_true @extended_tests_part_1 @animated_card
  Scenario Outline: Credit card recognition for <card_type> and validate date on animated card
    When User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>" and cvv "<cvv>"
    Then User will see card icon connected to card type <card_type>
    And User will see the same provided data on animated credit card "<formatted_card_number>", "<expiration_date>" and "<cvv>"
    And User will see that animated card is flipped, except for "AMEX"
    @smoke_test
    Examples:
      | card_number      | formatted_card_number | expiration_date | cvv | card_type |
      | 4111110000000211 | 4111 1100 0000 0211   | 12/22           | 123 | VISA      |
    Examples:
      | card_number     | formatted_card_number | expiration_date | cvv  | card_type |
      | 340000000000611 | 3400 000000 00611     | 12/23           | 1234 | AMEX      |
#      | 6011000000000301 | 6011 0000 0000 0301 | 12/23          | 123  | DISCOVER   |
#      | 3528000000000411 | 3528 0000 0000 0411 | 12/23          | 123  | JCB        |
#      | 5000000000000611 | 5000 0000 0000 0611 | 12/23          | 123  | MAESTRO    |
#      | 5100000000000511 | 5100 0000 0000 0511 | 12/23          | 123  | MASTERCARD |
#      | 3089500000000000021 | 3089 5000 0000 0000021 | 12/23          | 123 | PIBA         |
#      | 1801000000000901    | 1801 0000 0000 0901    | 12/23          | 123 | ASTROPAYCARD |
#      | 3000000000000111    | 3000 000000 000111     | 12/23          | 123 | DINERS       |

  @base_config @smoke_test @extended_tests_part_1
  Scenario: Disabled CVV field for PIBA card type
    When User fills payment form with credit card number "3089500000000000021", expiration date "12/23"
    Then User will see that "SECURITY_CODE" field is disabled

  @base_config @smoke_test @extended_tests_part_1
  Scenario: Submit payment form without data - fields validation
    When User clicks Pay button
    Then User will see validation message "Field is required" under all fields
    And User will see that all fields are highlighted
    And AUTH and THREEDQUERY requests were not sent

  @base_config @extended_tests_part_1 @fields_validation
  Scenario Outline: Filling payment form with empty fields -> cardNumber "<card_number>" expiration: "<expiration>", cvv: "<cvV>"
    When User fills payment form with incorrect or missing data: card number "<card_number>", expiration date "<expiration>" and cvv "<cvv>"
    And User clicks Pay button
    Then User will see "Field is required" message under field: "<field>"
    And User will see that "<field>" field is highlighted
    And AUTH and THREEDQUERY requests were not sent
    @smoke_test
    Examples:
      | card_number | expiration | cvv | field       |
      | None        | 12/22      | 123 | CARD_NUMBER |
    Examples:
      | card_number      | expiration | cvv  | field           |
      | 4000000000001000 | None       | 123  | EXPIRATION_DATE |
      | 4000000000001000 | 12/22      | None | SECURITY_CODE   |

  @base_config @fields_validation
  Scenario Outline: Filling payment form with incomplete data (frontend validation) -> cardNumber "<card_number>", expiration: "<expiration>", cvv: "<cvv>"
    When User fills payment form with incorrect or missing data: card number "<card_number>", expiration date "<expiration>" and cvv "<cvv>"
    And User clicks Pay button
    And User will see "Value mismatch pattern" message under field: "<field>"
    And User will see that "<field>" field is highlighted
    And AUTH and THREEDQUERY requests were not sent
    @smoke_test
    Examples:
      | card_number      | expiration | cvv | field         |
      | 4000000000001000 | 12/22      | 12  | SECURITY_CODE |
    @extended_tests_part_1
    Examples:
      | card_number      | expiration | cvv | field           |
      | 40000000         | 12/22      | 123 | CARD_NUMBER     |
      | 4000000000001000 | 12         | 123 | EXPIRATION_DATE |
    Examples:
      | card_number      | expiration | cvv | field           |
      | 4000000000009999 | 12/22      | 123 | CARD_NUMBER     |
      | 4000000000001000 | 44/22      | 123 | EXPIRATION_DATE |

  @base_config @fields_validation
  Scenario Outline: Filling payment form with incomplete data (backend validation) -> cardNumber "<card_number>", expiration: "<expiration>", cvv: "<cvv>"
    When User fills payment form with incorrect or missing data: card number "<card_number>", expiration date "<expiration>" and cvv "<cvv>"
    And InvalidField response set for "<field>"
    And User clicks Pay button
    Then User will see notification frame with message: "Invalid field"
    And User will see that notification frame has "red" color
    And User will see "Invalid field" message under field: "<field>"
    And User will see that "<field>" field is highlighted
    And THREEDQUERY request was sent only once with correct data
    @extended_tests_part_1
    Examples:
      | card_number      | expiration | cvv | field       |
      | 4000000000001000 | 12/22      | 123 | CARD_NUMBER |
    Examples:
      | card_number      | expiration | cvv | field           |
      | 4000000000001000 | 12/15      | 123 | EXPIRATION_DATE |
      | 4000000000001000 | 12/22      | 000 | SECURITY_CODE   |

  @base_config @extended_tests_part_1 @fields_validation
  Scenario: Filling 3-number of cvv code for AMEX card
    When User fills payment form with credit card number "340000000000611", expiration date "12/22" and cvv "123"
    And User clicks Pay button
    And User will see "Value mismatch pattern" message under field: "SECURITY_CODE"
    And AUTH and THREEDQUERY requests were not sent

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

  @base_config @translations
  Scenario Outline: Checking translations of labels and fields error for <language>
    When User changes page language to "<language>"
    And User clicks Pay button
    Then User will see all labels displayed on page translated into "<language>"
    And User will see validation message "Field is required" under all fields translated into "<language>"
    @smoke_test @extended_tests_part_1
    Examples:
      | language |
      | de_DE    |
    Examples:
      | language |
      | en_GB    |
#      | fr_FR    |
#      | en_US    |
#      | cy_GB    |
#      | da_DK    |
#      | es_ES    |
#      | nl_NL    |
#      | no_NO    |
#      | sv_SE    |

  @config_animated_card_true @animated_card @extended_tests_part_1 @translations
  Scenario Outline: Checking animated card translation for <language>
    When User changes page language to "<language>"
    And User fills payment form with credit card number "340000000000611", expiration date "12/22" and cvv "123"
    Then User will see that labels displayed on animated card are translated into "<language>"
    Examples:
      | language |
      | de_DE    |

  @base_config @extended_tests_part_1 @translations
  Scenario Outline: Checking translation of fields validation for <language>
    When User changes page language to "<language>"
    And User fills payment form with credit card number "4000000000000051 ", expiration date "12/22" and cvv "12"
    And User clicks Pay button
    Then User will see validation message "Value mismatch pattern" under "SECURITY_CODE" field translated into <language>
    Examples:
      | language |
      | fr_FR    |
#      | de_DE    |

  @base_config @translations
  Scenario Outline: Checking translation of backend fields validation for <language>
    When User changes page language to "<language>"
    And User fills payment form with credit card number "4000000000001059", expiration date "01/22" and cvv "123"
    And InvalidField response set for "CARD_NUMBER"
    And User clicks Pay button
    Then User will see "Invalid field" payment status translated into "<language>"
    Then User will see validation message "Invalid field" under "CARD_NUMBER" field translated into <language>
    Examples:
      | language |
      | es_ES    |
#      | de_DE    |

  @base_config @extended_tests_part_1 @translations
  Scenario Outline: Cardinal Commerce - checking "Success" status translation for <language>
    When User changes page language to "<language>"
    And User fills payment form with credit card number "4000000000001059", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see "Payment has been successfully processed" payment status translated into "<language>"
    And AUTH and THREEDQUERY requests were sent only once with correct data
    Examples:
      | language |
      | no_NO    |
#    Examples:
#      | language |
#      | de_DE    |

  @config_immediate_payment @extended_tests_part_1
  Scenario Outline: Immediate payment (card enrolled Y) - checking payment status for <action_code> response code
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "<action_code>"
    And User opens payment page
    Then User will see payment status information: "<payment_status_message>"
    And AUTH and THREEDQUERY requests were sent only once with correct data
    @smoke_test
    Examples:
      | action_code | payment_status_message                  |
      | OK          | Payment has been successfully processed |
    Examples:
      | action_code | payment_status_message |
      | DECLINE     | Decline                |

  @config_immediate_payment
  Scenario: Immediate payment (card enrolled N) - checking payment status for OK response code
    When THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_immediate_payment
  Scenario: Immediate payment (card enrolled Y) - check ACS response for code: FAILURE
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "FAILURE"
    And User opens payment page
    Then User will see payment status information: "Wystąpił błąd"
    And THREEDQUERY request was sent only once with correct data

  @config_immediate_payment_and_submit_on_success @smoke_test @extended_tests_part_1
  Scenario: Immediate payment with submitOnSuccess - successful payment
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_skip_jsinit @cardinal_commerce
  Scenario: Successful payment with skipped JSINIT process
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
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

  @config_default
  Scenario: Checking that 'submitOnSuccess' is enabled by default
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_submit_on_error_true @smoke_test @extended_tests_part_1
  Scenario: Cardinal Commerce - error payment with enabled 'submit on error' process
    When User fills merchant data with name "John Test", email "test@example", phone "44422224444"
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "DECLINE"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_field_style @smoke_test @extended_tests_part_1
  Scenario: Checking style of individual fields
    Then User will see that "CARD_NUMBER" field has correct style
    And User will see that "EXPIRATION_DATE" field has correct style

  @config_field_style @smoke_test @extended_tests_part_2
  Scenario: Checking style of notification frame
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see that "NOTIFICATION_FRAME" field has correct style

  @config_update_jwt_true @smoke_test @extended_tests_part_2
  Scenario: Successful payment with updated JWT
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And User fills amount field
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_defer_init
  Scenario: Successful payment with deferInit
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And JSINIT request was not sent
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    Then JSINIT request was sent only once
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_defer_init
  Scenario: Successful payment with deferInit and updated JWT
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And User fills amount field
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    And JSINIT requests contains updated jwt

  @config_submit_cvv_only @extended_tests_part_2
  Scenario: Successful payment when cvv field is selected to submit
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will not see CARD_NUMBER
    And User will not see EXPIRATION_DATE
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_submit_cvv_for_amex @extended_tests_part_2
  Scenario: Successful payment by AMEX when cvv field is selected to submit
    When User fills "SECURITY_CODE" field "1234"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will not see CARD_NUMBER
    And User will not see EXPIRATION_DATE
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_cvvToSubmit_and_submitOnSuccess @extended_tests_part_2
  Scenario: Successful payment with fieldToSubmit and submitOnSuccess
    When User fills "SECURITY_CODE" field "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User is redirected to action page
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_bypass_cards @bypass_cards
  Scenario: Successful payment with bypassCard
    When User fills payment form with credit card number "3528000000000411", expiration date "12/30" and cvv "123"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH request was sent only once with correct data

  @config_requestTypes_tdq
  Scenario: Successful payment with request types: THREEDQUERY
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data

  @config_requestTypes_tdq_auth
  Scenario: Successful payment with request types: THREEDQUERY, AUTH
    When User fills payment form with credit card number "4000000000001091", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @config_requestTypes_acheck_tdq_auth
  Scenario: Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_requestTypes_tdq_auth_riskdec
  Scenario: Successful payment with additional request types: THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data
    And AUTH, RISKDEC ware sent only once in one request

  @config_requestTypes_riskdec_acheck_tdq_auth
  Scenario: Successful payment with additional request types: RISKDEC, ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And RISKDEC, ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH request was sent only once with correct data

  @config_requestTypes_acheck_tdq_auth_riskdec
  Scenario: Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
    And AUTH, RISKDEC ware sent only once in one request

  @config_immediate_payment_tdq
  Scenario: Immediate payment - Successful payment with request types: THREEDQUERY
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with correct data

  @config_immediate_payment_acheck_tdq_auth_riskdec
  Scenario: Immediate payment - Successful payment with additional request types: ACCOUNTCHECK, THREEDQUERY, AUTH, RISKDEC
    And ACCOUNTCHECK, THREEDQUERY mock response is set to OK
    And ACS mock response is set to "OK"
    And AUTH, RISKDEC mock response is set to OK
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And ACCOUNTCHECK, THREEDQUERY ware sent only once in one request
#    ToDo
#    And AUTH, RISKDEC ware sent only once in one request

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

  @config_bypass_cards_tdq_auth
  Scenario: Successful payment with bypassCard and custom request types: THREEDQUERY, AUTH
    When User fills payment form with credit card number "4000000000001026", expiration date "12/30" and cvv "123"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH ware sent only once in one request

  @config_bypass_cards_acheck_tdq_auth
  Scenario: Successful payment with bypassCard and custom request types: ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with credit card number "4000000000001026", expiration date "12/30" and cvv "123"
    And User clicks Pay button - ACCOUNTCHECK, AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And ACCOUNTCHECK, AUTH ware sent only once in one request

  @config_bypass_cards_riskdec_acheck_tdq_auth @extended_tests_part_2
  Scenario: Successful payment with bypassCard and custom request types: RISKDEC, ACCOUNTCHECK, THREEDQUERY, AUTH
    When User fills payment form with credit card number "4000000000001026", expiration date "12/30" and cvv "123"
    And User clicks Pay button - RISKDEC, ACCOUNTCHECK, AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And RISKDEC, ACCOUNTCHECK, AUTH ware sent only once in one request

  @config_bypass_cards_tdq_auth_riskdec
  Scenario: Successful payment with bypassCard and custom request types: THREEDQUERY, AUTH, RISKDEC
    When User fills payment form with credit card number "4000000000001026", expiration date "12/30" and cvv "123"
    And User clicks Pay button - AUTH, RISKDEC response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And THREEDQUERY request was not sent
    And AUTH, RISKDEC ware sent only once in one request

  @base_config @extended_tests_part_2
  Scenario Outline: Checking <action_code> callback functionality
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    And User will see "<callback_popup>" popup
    @smoke_test
    Examples:
      | action_code | callback_popup |
      | OK          | success        |
    Examples:
      | action_code | callback_popup |
      | DECLINE     | error          |

  @base_config @extended_tests_part_2
  Scenario: Checking callback function for in-browser validation
    When User clicks Pay button
    And User will see "error" popup

  @config_incorrect_request_type @extended_tests_part_2
  Scenario: Checking request types validation
    When User sets incorrect request type in config file
    Then User will see that application is not fully loaded

  @base_config @parent_iframe @extended_tests_part_2
  Scenario Outline: App is embedded in another iframe - Cardinal Commerce test
    When User opens payment page
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will see payment status information: "<payment_status_message>"
    And User will see that notification frame has "<color>" color
    And AUTH and THREEDQUERY requests were sent only once with correct data
    @smoke_test
    Examples:
      | action_code | payment_status_message                  | color |
      | OK          | Payment has been successfully processed | green |
    Examples:
      | action_code     | payment_status_message | color |
      | UNAUTHENTICATED | Unauthenticated        | red   |

  @config_animated_card_true @parent_iframe @animated_card @extended_tests_part_2
  Scenario Outline: App is embedded in another iframe - animated card test
    When User opens payment page
    And User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>" and cvv "<cvv>"
    Then User will see card icon connected to card type <card_type>
    And User will see the same provided data on animated credit card "<formatted_card_number>", "<expiration_date>" and "<cvv>"
    And User will see that animated card is flipped, except for "AMEX"
    Examples:
      | card_number      | formatted_card_number | expiration_date | cvv | card_type |
      | 4111110000000211 | 4111 1100 0000 0211   | 12/22           | 123 | VISA      |

  @base_config @parent_iframe
  Scenario: App is embedded in another iframe - fields validation test
    When User opens payment page
    And User clicks Pay button
    Then User will see validation message "Field is required" under all fields
    And User will see that all fields are highlighted
    And AUTH and THREEDQUERY requests were not sent

  @config_placeholders @smoke_test @extended_tests_part_2
  Scenario: Checking placeholders in input fields
    Then User will see specific placeholders in input fields: Card number, Exp date, CVV

  @base_config
  Scenario: Checking default placeholders in input fields
    Then User will see default placeholders in input fields: ***** ***** ***** *****, MM/YY, ***

  @base_config @extended_tests_part_2
  Scenario: Checking default cvv placeholder for AMEX card
    When User fills payment form with credit card number "340000000000611", expiration date "12/23"
    Then User will see '****' placeholder in security code field

  @base_config @extended_tests_part_2
  Scenario Outline: Checking <card_type> card icon displayed in input field
    When User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>"
    Then User will see "<card_type>" icon in card number input field
    @smoke_test
    Examples:
      | card_number      | expiration_date | card_type |
      | 4111110000000211 | 12/22           | VISA      |
    Examples:
      | card_number     | expiration_date | card_type |
      | 340000000000611 | 12/23           | AMEX      |
#      | 6011000000000301    | 12/23           | DISCOVER     |
#      | 3528000000000411    | 12/23           | JCB          |
#      | 5000000000000611    | 12/23           | MAESTRO      |
#      | 5100000000000511    | 12/23           | MASTERCARD   |
#      | 3089500000000000021 | 12/23           | PIBA         |
#      | 1801000000000901    | 12/23           | ASTROPAYCARD |
#      | 3000000000000111    | 12/23           | DINERS       |

  @config_default
  Scenario: Checking that animated card and card icon are not displayed by default
    When User fills payment form with credit card number "4111110000000211", expiration date "12/23"
    Then User will not see ANIMATED_CARD
    And User will not see CARD_ICON

  @base_config
  Scenario: Verify number on JSINIT requests
    Then JSINIT request was sent only once

  @config_notifications_false @extended_tests_part_1
  Scenario: Notification frame is not displayed after payment
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will not see notification frame

  @config_submit_on_success_and_error_true
  Scenario Outline: Notification frame is not displayed after payment with submitOn<submitOn>
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "<action_code>"
    Then User will not see notification frame
    Examples:
      | submitOn | action_code |
      | Success  | OK          |
      | Error    | DECLINE     |

  @config_cybertonica @extended_tests_part_2
  Scenario: Cybertonica - 'fraudcontroltransactionid' flag is added to THREEDQUERY and AUTH requests during payment
    When User fills payment form with credit card number "4111111111111111", expiration date "12/30" and cvv "123"
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with 'fraudcontroltransactionid' flag
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag

  @base_config
  Scenario: Cybertonica - 'fraudcontroltransactionid' flag is not added to THREEDQUERY and AUTH requests during payment
    When User fills payment form with credit card number "4000000000001059", expiration date "01/22" and cvv "123"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_N"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once without 'fraudcontroltransactionid' flag
    And AUTH request was sent only once without 'fraudcontroltransactionid' flag

  @config_cybertonica_bypass_cards
  Scenario: Cybertonica - 'fraudcontroltransactionid' flag is added to AUTH requests during payment with bypass_pass
    When User fills payment form with credit card number "3528000000000411", expiration date "12/30" and cvv "123"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag
    And THREEDQUERY request was not sent

  @config_cybertonica_immediate_payment
  Scenario: Cybertonica - 'fraudcontroltransactionid' flag is added to THREEDQUERY and AUTH requests during 'immediate payment'
    When THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"
    And THREEDQUERY request was sent only once with 'fraudcontroltransactionid' flag
    And AUTH request was sent only once with 'fraudcontroltransactionid' flag