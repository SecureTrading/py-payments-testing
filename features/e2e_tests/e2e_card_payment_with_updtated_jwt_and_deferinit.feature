Feature: E2E Card Payments with updated jwt for deferinit config

  As a user
  I want to use card payments method
  In order to check full payment functionality with updated jwt

  Scenario: Successful payment with updated jwt and deferinit true
    Given JS library is configured with DEFER_INIT_CONFIG and BASE_JWT
    And User opens example page WITH_UPDATE_JWT
    When User calls updateJWT function by filling amount field
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color