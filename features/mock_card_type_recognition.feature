Feature: Payments Card recognition

  As a user
  I want to use card payments method
  In order to check that card is properly recognized

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_animated_card_true @animated_card
  Scenario Outline: Credit card recognition for <card_type> and validate date on animated card
    When User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>" and cvv "<cvv>"
    Then User will see card icon connected to card type <card_type>
    And User will see the same provided data on animated credit card "<formatted_card_number>", "<expiration_date>" and "<cvv>"
    And User will see that animated card is flipped, except for "AMEX"

    @smoke_test
    Examples:
      | card_number      | formatted_card_number | expiration_date | cvv | card_type |
      | 4111110000000211 | 4111 1100 0000 0211   | 12/22           | 123 | VISA      |

    @extended_tests_part_1
    Examples:
      | card_number     | formatted_card_number | expiration_date | cvv  | card_type |
      | 340000000000611 | 3400 000000 00611     | 12/23           | 1234 | AMEX      |

    Examples:
      | card_number         | formatted_card_number  | expiration_date | cvv | card_type    |
      | 6011000000000301    | 6011 0000 0000 0301    | 12/23           | 123 | DISCOVER     |
      | 3528000000000411    | 3528 0000 0000 0411    | 12/23           | 123 | JCB          |
      | 5000000000000611    | 5000 0000 0000 0611    | 12/23           | 123 | MAESTRO      |
      | 5100000000000511    | 5100 0000 0000 0511    | 12/23           | 123 | MASTERCARD   |
      | 3000000000000111    | 3000 000000 000111     | 12/23           | 123 | DINERS       |
      | 1801000000000901    | 1801 0000 0000 0901    | 12/23           | 123 | ASTROPAYCARD |

  @base_config @smoke_test @extended_tests_part_1
  Scenario: Disabled CVV field for PIBA card type and card recognition
    When User fills payment form with credit card number "3089500000000000021", expiration date "12/23"
    Then User will see that "SECURITY_CODE" field is disabled
    And User will see "PIBA" icon in card number input field