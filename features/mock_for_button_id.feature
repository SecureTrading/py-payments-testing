Feature: E2E for buttonID
  As a user
  I want to use config with button id
  In order to check payment

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag

  @base_config
  Scenario: Request was sent
    Given User opens prepared example page for mock WITH_ADDITIONAL_BUTTON
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    When User fills payment form with defined card VISA_CARD
    And User clicks Pay button - AUTH response is set to "OK"
    And AUTH request was sent only once with correct data

  @e2e_button_id_config
  Scenario: Request was not sent
    Given User opens prepared example page for mock WITH_ADDITIONAL_BUTTON
    When User fills payment form with defined card VISA_CARD
    And User clicks Additional button
    Then AUTH and THREEDQUERY requests were not sent
