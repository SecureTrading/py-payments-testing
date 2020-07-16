Feature: E2E tests
  As a user
  I want to use card payments method
  In order to check full payment functionality

  #ToDO - Work in progress
  #remove sleep before cardinal modal
  Background:
#    Given JavaScript configuration is set for scenario based on scenario's @config tag
    Given User opens page with payment form

  @base_config @cardinal_commerce_v2.0
  Scenario: Successful Frictionless Authentication - MasterCard
    When User fills payment form with credit card number "5200000000001005", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    Then User will see that Submit button is "disabled" after payment
    And User will see that all input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Failed Frictionless Authentication - Visa
    When User fills payment form with credit card number "4000000000001018", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color
    Then User will see that Submit button is "enabled" after payment
    And User will see that all input fields are "enabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Attempts Stand-In Frictionless Authentication - Visa
    When User fills payment form with credit card number "4000000000001026", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    Then User will see that Submit button is "disabled" after payment
    And User will see that all input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Unavailable Frictionless Authentication from the Issuer - MasterCard
    When User fills payment form with credit card number "5200000000001039", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    Then User will see that Submit button is "disabled" after payment
    And User will see that all input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Rejected Frictionless Authentication by the Issuer - Visa
    When User fills payment form with credit card number "4000000000001042", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Authentication Not Available on Lookup - MasterCard
    When User fills payment form with credit card number "5200000000001054", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Error on Lookup - Visa
    When User fills payment form with credit card number "4000000000001067", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Bank System Error"
    And User will see that notification frame has "red" color

  #ToDo - increase timeout
  @base_config @cardinal_commerce_v2.0
  Scenario: Timeout on cmpi_lookup Transaction - Visa
    When User fills payment form with credit card number "4000000000001075", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Bypassed Authentication - MasterCard
    When User fills payment form with credit card number "5200000000001088", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Successful Step Up Authentication - Visa
    When User fills payment form with credit card number "4000000000001091", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User fills authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Failed Step Up Authentication - MasterCard
    When User fills payment form with credit card number "5200000000001104", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User fills authentication modal
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Step Up Authentication is Unavailable - Visa
    When User fills payment form with credit card number "4000000000001117", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User fills authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Require MethodURL - Visa
    When User fills payment form with credit card number "4000010000000001", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User fills authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Prompt for Whitelist - MasterCard
    When User fills payment form with credit card number "5200000000002003", expiration date "12/30" and cvv "123"
    And User clicks Pay button
    And User fills authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color