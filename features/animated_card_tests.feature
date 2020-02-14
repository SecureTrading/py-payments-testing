Feature: Animated Card tests
  As a user
  I want to check payment card functionality and
  input fields validation

  Background:
    Given User opens page with animated card

  @animated_card_repo_test
  Scenario Outline: Credit card recognition for <card_type> and validate date on animated card
    When User fills payment form with data: "<card_number>", "<expiration_date>" and "<cvv>"
    Then User will see card icon connected to card type <card_type>
    And User will see the same provided data on animated credit card "<formatted_card_number>", "<expiration_date>" and "<cvv>"
    And User will see that animated card is flipped, except for "AMEX"
    Examples:
      | card_number      | formatted_card_number | expiration_date | cvv  | card_type    |
      | 340000000000611  | 3400 000000 00611     | 12/23           | 1234 | AMEX         |
      | 4111110000000211 | 4111 1100 0000 0211   | 12/22           | 123  | VISA         |
      | 1801000000000901 | 1801 0000 0000 0901   | 12/23           | 123  | ASTROPAYCARD |
      | 3000000000000111 | 3000 000000 000111    | 12/23           | 123  | DINERS       |
      | 6011000000000301 | 6011 0000 0000 0301   | 12/23           | 123  | DISCOVER     |
      | 3528000000000411 | 3528 0000 0000 0411   | 12/23           | 123  | JCB          |
      | 5000000000000611 | 5000 0000 0000 0611   | 12/23           | 123  | MAESTRO      |
      | 5100000000000511 | 5100 0000 0000 0511   | 12/23           | 123  | MASTERCARD   |

  @animated_card_repo_test
  Scenario: Credit card recognition for PIBA and validate date on animated card
    When User fills payment form with data: "3089500000000000021", "12/23"
    Then User will see card icon connected to card type PIBA
    And User will see the same provided data on animated credit card "3089 5000 0000 0000021", "12/23"
    Then User will see "SECURITY_CODE" field is disabled

  @animated_card_repo_test
  Scenario Outline: Checking animated card translation for <language>
    When User fills payment form with data: "340000000000611", "12/22" and "123"
    Then User will see that labels displayed on animated card are translated into "<language>"
    Examples:
      | language |
      | en_GB    |
  #      | es_ES    |
  #      | sv_SE    |

  @animated_card_repo_test
  Scenario Outline: Filling payment form with empty fields -> cardNumber "<card_number>", expiration: "<expiration_date>", cvv: "<cvv>"
    When User fills payment form with data: "<card_number>", "<expiration_date>" and "<cvv>"
    And User changes the field focus
    Then User will see "Field is required" message under no-iframe-field: "<field>"
    And User will see that "<field>" no-iframe-field is highlighted
    Examples:
      | card_number      | expiration_date | cvv  | field           |
      | None             | 12/22           | 123  | CARD_NUMBER     |
      | 4000000000001000 | None            | 123  | EXPIRATION_DATE |
      | 4000000000001000 | 12/22           | None | SECURITY_CODE   |

  @animated_card_repo_test
  Scenario: Filling 3-number of cvc code for AMEX card
    When User fills payment form with data: "340000000000611", "12/22" and "123"
    And User changes the field focus
    Then User will see "Value mismatch pattern" message under no-iframe-field: "SECURITY_CODE"

  @animated_card_repo_test
  Scenario Outline: Filling payment form with incomplete data (frontend validation) -> cardNumber "<card_number>", expiration: "<expiration>", cvv: "<cvv>"
    When User fills payment form with data: "<card_number>", "<expiration>" and "<cvv>"
    And User changes the field focus
    Then User will see "Value mismatch pattern" message under no-iframe-field: "<field>"
    And User will see that "<field>" no-iframe-field is highlighted
    Examples:
      | card_number      | expiration | cvv | field           |
      | 4000000000001000 | 12/22      | 12  | SECURITY_CODE   |
      | 40000000         | 12/22      | 123 | CARD_NUMBER     |
      | 4000000000001000 | 12         | 123 | EXPIRATION_DATE |
      | 4000000000009999 | 12/22      | 123 | CARD_NUMBER     |
      | 4000000000001000 | 44/22      | 123 | EXPIRATION_DATE |