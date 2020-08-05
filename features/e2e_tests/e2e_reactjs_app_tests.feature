Feature: E2E Successfull payments on reactjs app

  As a user
  I want to use card payments method embeded on reactjs pages
  In order to check full payment functionality

  Background:
    Given User opens reactjs app page with payment form

  @base_config
  Scenario: React app - successfully processed payments with tabs change
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    And Success notification with Payment has been successfully processed message is displayed
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then Success notification with Payment has been successfully processed message is displayed

  @e2e_config_defer_init_true
  Scenario: React app - successfully processed payments with tabs change and and deferinit config
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    And Success notification with Payment has been successfully processed message is displayed
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Payment' in reactjs app
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then Success notification with Payment has been successfully processed message is displayed

  @e2e_config_update_jwt_true
  Scenario: React app - successfully processed payments with tabs change and update JWT
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    And Success notification with Payment has been successfully processed message is displayed
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then Success notification with Payment has been successfully processed message is displayed

  @base_config
  Scenario: React app - decline payment and then successful payment
    And User fills payment form with defined card MASTERCARD_DECLINED_CARD
    And User clicks Pay button
    And Success notification with Decline message is displayed
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Home' in reactjs app
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then Success notification with Payment has been successfully processed message is displayed

  @base_config
  Scenario: React app - successfully processed payment after change tabs
    When User switch tab to 'Personal Data' in reactjs app
    And User switch tab to 'Payment' in reactjs app
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then Success notification with Payment has been successfully processed message is displayed