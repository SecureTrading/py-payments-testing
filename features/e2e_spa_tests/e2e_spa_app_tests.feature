@reactJS
@angular
Feature: E2E Successfull payments on SPA app

  As a user
  I want to use card payments method embeded on SPA example pages
  In order to check full payment functionality

  Scenario: SPA app - successfully processed payments with tabs change
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    And User will see payment status information: "Payment has been successfully processed"
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"

  Scenario: SPA app - successfully processed payments with tabs change and and deferinit config
    Given JS library is configured with DEFER_INIT_CONFIG and BASE_JWT
    And User opens example page
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    And User will see payment status information: "Payment has been successfully processed"
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Payment' in reactjs app
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"

  Scenario: SPA app - successfully processed payments with tabs change and update JWT
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    And User calls updateJWT function by filling amount field
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    And User will see payment status information: "Payment has been successfully processed"
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"

  Scenario: SPA app - decline payment and then successful payment
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    And User fills payment form with defined card MASTERCARD_DECLINED_CARD
    And User clicks Pay button
    And User will see payment status information: "Decline"
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"

  Scenario: SPA app - successfully processed payment after change tabs
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Payment' in reactjs app
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"