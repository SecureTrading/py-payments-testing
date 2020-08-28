Feature:Animated card translations

  As a user
  I want to use card payments method
  In order to check animated card functionality in various languages

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens page with payment form

  @config_animated_card_true @animated_card @translations
  Scenario Outline: Checking animated card translation for <language>
    When User changes page language to "<language>"
    And User fills payment form with credit card number "340000000000611", expiration date "12/22" and cvv "123"
    Then User will see that labels displayed on animated card are translated into "<language>"
    @extended_tests_part_1
    Examples:
      | language |
      | de_DE    |
    Examples:
      | language |
      | en_GB    |
      | fr_FR    |
      | en_US    |
      | cy_GB    |
      | da_DK    |
      | es_ES    |
      | nl_NL    |
      | no_NO    |
      | sv_SE    |