Feature: E2E Cybertonica

  As a user
  I want to use card payments method with cybertonica config
  In order to check full payment functionality

  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment
    Given JWT token is prepared
    And User opens page with payment form
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"

  @e2e_config_cybertonica_bypass_cards
  Scenario: Cybertonica - successfull payment with bypass_pass
    Given JWT token is prepared
    And User opens page with payment form
    When User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment with startOnLoad
    Given JWT token with startOnLoad is prepared
    And User opens page with payment form
    When User fills payment form with defined card JCB_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"