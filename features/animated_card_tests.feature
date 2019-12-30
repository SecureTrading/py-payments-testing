Feature: Payment methods
  As a user
  I want to use various payment methods using correct and incorrect credentials
  In order to check full payment functionality

  Background:
    Given "payment_methods" page is open

  Scenario:
    When User fills payment form with credit card number "4111110000000211", expiration date "12/30" and cvv "123"
    And User clicks Pay button