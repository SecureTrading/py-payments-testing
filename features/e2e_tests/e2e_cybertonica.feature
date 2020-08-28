Feature: E2E Cybertonica

  As a user
  I want to use card payments method with cybertonica config
  In order to check full payment functionality

  @reactJS
  @angular
  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment
    Given JS library is configured with CYBERTONICA_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_AUTH_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"

  @e2e_config_cybertonica_bypass_cards
  Scenario: Cybertonica - successfull payment with bypass_pass
    Given JS library is configured with CYBERTONICA_WITH_BYPASSCARDS_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment with startOnLoad
    Given JS library is configured with CYBERTONICA_START_ON_LOAD_CONFIG and JWT_WITH_NON_FRICTIONLESS_CARD
    And User opens example page WITHOUT_SUBMIT_BUTTON
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"