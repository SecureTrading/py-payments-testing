Feature: Payment form validations

  As a user
  I want to use card payments method
  In order to check payment form validations

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @base_config @smoke_test @extended_tests_part_1
  Scenario: Submit payment form without data - fields validation
    When User clicks Pay button
    Then User will see validation message "Field is required" under all fields
    And User will see that all fields are highlighted
    And AUTH and THREEDQUERY requests were not sent

  @config_submit_cvv_only
  Scenario: Checking validation if only Security code field is enabled
    When User clicks Pay button
    Then User will see "Field is required" message under field: "SECURITY_CODE"
    And User will see that "SECURITY_CODE" field is highlighted
    And AUTH and THREEDQUERY requests were not sent

  @base_config @fields_validation
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

    @extended_tests_part_1
    Examples:
      | card_number      | expiration | cvv | field           |
      | 4000000000001000 | None       | 123 | EXPIRATION_DATE |

    Examples:
      | card_number      | expiration | cvv  | field         |
      | 4000000000001000 | 12/22      | None | SECURITY_CODE |

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