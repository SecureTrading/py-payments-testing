Feature: Payment form styles check

  As a user
  I want to use card payments method
  In order to check full payment functionality with proper UI styling

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

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

  @base_config
  Scenario Outline: Checking <card_type> card icon displayed in input field
    When User fills payment form with credit card number "<card_number>", expiration date "<expiration_date>"
    Then User will see "<card_type>" icon in card number input field

    @smoke_test @extended_tests_part_2
    Examples:
      | card_number      | expiration_date | card_type |
      | 4111110000000211 | 12/22           | VISA      |

    Examples:
      | card_number         | expiration_date | card_type    |
      | 340000000000611     | 12/23           | AMEX         |
      | 6011000000000301    | 12/23           | DISCOVER     |
      | 3528000000000411    | 12/23           | JCB          |
      | 5000000000000611    | 12/23           | MAESTRO      |
      | 5100000000000511    | 12/23           | MASTERCARD   |
      | 3089500000000000021 | 12/23           | PIBA         |
      | 1801000000000901    | 12/23           | ASTROPAYCARD |
      | 3000000000000111    | 12/23           | DINERS       |

  @config_default
  Scenario: Checking that animated card and card icon are not displayed by default
    When User fills payment form with credit card number "4111110000000211", expiration date "12/23"
    Then User will not see ANIMATED_CARD
    And User will not see CARD_ICON