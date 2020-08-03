Feature: E2E Cybertonica

  As a user
  I want to use card payments method with cybertonica config
  In order to check full payment functionality

  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment
    Given JWT token is prepared
    Given User opens page with payment form
    When User fills payment form with credit card number "4111111111111111", expiration date "12/30" and cvv "123"
    When User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"

  @e2e_config_cybertonica_bypass_cards
  Scenario: Cybertonica - successfull payment with bypass_pass
    Given JWT token is prepared
    Given User opens page with payment form
    When User fills payment form with credit card number "3528000000000411", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_config_cybertonica
  Scenario: Cybertonica - successfull payment with startOnLoad
    Given JWT token with startOnLoad is prepared
    Given User opens page with payment form
    When User fills payment form with credit card number "3528000000000411", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User opens payment page
    Then User will see payment status information: "Payment has been successfully processed"