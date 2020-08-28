Feature: Cardinal Commerce E2E tests
  As a user
  I want to use card payments method
  In order to check Cardinal Commerce integration

  Background:
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page

  @reactJS
  @angular
  @e2e_cardinal_commerce_v1
  Scenario: Successful Authentication
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_AUTH_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @e2e_cardinal_commerce_v1
  Scenario: Failed Signature
    When User fills payment form with defined card VISA_FAILED_SIGNATURE_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color
    And User will see that Submit button is "enabled" after payment
    And User will see that ALL input fields are "enabled"

  @e2e_cardinal_commerce_v1
  Scenario: Failed Authentication
    When User fills payment form with defined card AMERICAN_EXPRESS_FAILED_AUTH_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color
    And User will see that Submit button is "enabled" after payment
    And User will see that ALL input fields are "enabled"

  @e2e_cardinal_commerce_v1
  Scenario: Attempts/Non-Participating
    When User fills payment form with defined card DISCOVER_PASSIVE_AUTH_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_cardinal_commerce_v1
  Scenario: Timeout
    When User fills payment form with defined card AMERICAN_EXPRESS_TIMEOUT_CARD
    And User clicks Pay button
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @e2e_cardinal_commerce_v1
  Scenario: Not Enrolled
    When User fills payment form with defined card MASTERCARD_NOT_ENROLLED_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_cardinal_commerce_v1
  Scenario: Unavailable
    When User fills payment form with defined card AMERICAN_EXPRESS_UNAVAILABLE_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_cardinal_commerce_v1
  Scenario: Merchant Not Active
    When User fills payment form with defined card VISA_MERCHANT_NOT_ACTIVE_CARD
    And User clicks Pay button
    Then User will see payment status information: "Bank System Error"
    And User will see that notification frame has "red" color

  @e2e_cardinal_commerce_v1
  Scenario: Cmpi lookup error
    When User fills payment form with defined card VISA_CMPI_LOOKUP_ERROR_CARD
    And User clicks Pay button
    Then User will see payment status information: "Bank System Error"
    And User will see that notification frame has "red" color

  @e2e_cardinal_commerce_v1
  Scenario: Cmpi authenticate error
    When User fills payment form with defined card MASTERCARD_CMPI_AUTH_ERROR_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @e2e_cardinal_commerce_v1
  Scenario: Authentication Unavailable
    When User fills payment form with defined card MASTERCARD_AUTH_UNAVAILABLE_CARD
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @e2e_cardinal_commerce_v1
  Scenario: Bypassed Authentication
    When User fills payment form with defined card DISCOVER_BYPASSED_AUTH_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color