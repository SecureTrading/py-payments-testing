Feature: Mock for button id
  As a user
  I want to open page with two buttons
  In order to check payment process for two buttons

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag
    And User opens prepared payment form page WITH_ADDITIONAL_BUTTON

  @base_config
  Scenario: Click on button configured as button id
    When User fills payment form with defined card VISA_CARD
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And User clicks Pay button - AUTH response is set to "OK"
    Then User will see payment status information: "Payment has been successfully processed"
    And AUTH and THREEDQUERY requests were sent only once with correct data

  @base_config
  Scenario: Click on button configured as additional button
    When User fills payment form with defined card VISA_CARD
    And THREEDQUERY mock response is set to "ENROLLED_Y"
    And ACS mock response is set to "OK"
    And AUTH response is set to "OK"
    And User clicks Additional button
    Then AUTH and THREEDQUERY requests were not sent
