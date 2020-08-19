Feature: E2E for buttonID
  As a user
  I want to use config with button id
  In order to check payment

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens prepared payment form page WITH_ADDITIONAL_BUTTON

  @base_config
  Scenario: Request was sent
    When User fills payment form with defined card VISA_CARD
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And User clicks Pay button - AUTH response is set to "OK"
    Then THREEDQUERY request was sent only once with correct data

  @base_config
  Scenario: Request was not sent
    When User fills payment form with defined card VISA_CARD
    And User clicks Additional button
    Then AUTH and THREEDQUERY requests were not sent
