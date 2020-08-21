Feature: Payment form styles check

  As a user
  I want to use inline config
  In order to check payment form functionality

  @inline_config
  Scenario: Checking that animated card and card icon are displayed
    Given JS library is configured with ANIMATED_CARD_PAN_ICON_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with credit card number "4111110000000211", expiration date "12/22" and cvv "123"
    Then User will see "VISA" icon in card number input field
    And User will see card icon connected to card type VISA
    And User will see the same provided data on animated credit card "4111 1100 0000 0211", "12/22" and "123"

  @inline_config
  Scenario: Checking placeholders in input fields
    Given JS library is configured with PLACEHOLDERS_CONFIG and BASE_JWT
    And User opens example page
    Then User will see specific placeholders in input fields: Number, Expiration, CVV

  @inline_config
  Scenario: Checking style of individual fields
    Given JS library is configured with STYLES_CONFIG and BASE_JWT
    When User opens example page
    Then User will see that CARD_NUMBER field has rgba(0, 0, 255, 1) color
    And User will see that EXPIRATION_DATE field has rgba(255, 0, 0, 1) color

  @inline_config
  Scenario: Check translation overwriting mechanism for Pay button and validation message
    Given JS library is configured with CUSTOM_TRANSLATION_CONFIG and BASE_JWT
    When User opens example page
    Then User will see that Pay button is translated into "KupTeraz!"

  @inline_config
  Scenario: Notification frame is not displayed after payment
    Given JS library is configured with DISABLE_NOTIFICATION_CONFIG and BASE_JWT
    When User opens example page
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame