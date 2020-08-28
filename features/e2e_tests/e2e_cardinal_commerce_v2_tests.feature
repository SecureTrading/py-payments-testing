Feature: Cardinal Commerce E2E tests
  As a user
  I want to use card payments method
  In order to check Cardinal Commerce integration

  Background:
    Given JS library is configured with BASIC_CONFIG and BASE_JWT
    And User opens example page

  @reactJS
  @angular
  @base_config @cardinal_commerce_v2.0
  Scenario: Successful Frictionless Authentication - MasterCard
    When User fills payment form with defined card MASTERCARD_SUCCESSFUL_FRICTIONLESS_AUTH
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Failed Frictionless Authentication - Visa
    When User fills payment form with defined card VISA_FAILED_FRICTIONLESS_AUTH
    And User clicks Pay button
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color
    And User will see that Submit button is "enabled" after payment
    And User will see that ALL input fields are "enabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Attempts Stand-In Frictionless Authentication - Visa
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Unavailable Frictionless Authentication from the Issuer - MasterCard
    When User fills payment form with defined card MASTERCARD_UNAVAILABLE_FRICTIONLESS_AUTH
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color
    And User will see that Submit button is "disabled" after payment
    And User will see that ALL input fields are "disabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Rejected Frictionless Authentication by the Issuer - Visa
    When User fills payment form with defined card VISA_REJECTED_FRICTIONLESS_AUTH
    And User clicks Pay button
    Then User will see payment status information: "Unauthenticated"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Authentication Not Available on Lookup - MasterCard
    When User fills payment form with defined card MASTERCARD_AUTH_NOT_AVAILABLE_ON_LOOKUP
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Error on Lookup - Visa
    When User fills payment form with defined card VISA_ERROR_ON_LOOKUP
    And User clicks Pay button
    Then User will see payment status information: "Bank System Error"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Timeout on cmpi_lookup Transaction - Visa
    When User fills payment form with defined card VISA_TIMEOUT_ON_CMPI_LOOKUP_TRANSACTION
    And User clicks Pay button
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Bypassed Authentication - MasterCard
    When User fills payment form with defined card MASTERCARD_BYPASSED_AUTH
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @reactJS
  @angular
  @base_config @cardinal_commerce_v2.0
  Scenario: Successful Step Up Authentication - Visa
    When User fills payment form with defined card VISA_NON_FRICTIONLESS
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Failed Step Up Authentication - MasterCard
    When User fills payment form with defined card MASTERCARD_FAILED_STEP_UP_AUTH
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Step Up Authentication is Unavailable - Visa
    When User fills payment form with defined card VISA_STEP_UP_AUTH_IS_UNAVAILABLE
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Error on Authentication - MasterCard
    When User fills payment form with defined card MASTERCARD_ERROR_ON_AUTH
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "An error occurred"
    And User will see that notification frame has "red" color
    And User will see that Submit button is "enabled" after payment
    And User will see that ALL input fields are "enabled"

  @base_config @cardinal_commerce_v2.0
  Scenario: Prompt for Whitelist - MasterCard
    When User fills payment form with defined card MASTERCARD_PROMPT_FOR_WHITELIST
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Pre-Whitelisted - Visabase_config
    When User fills payment form with defined card VISA_PRE_WHITELISTED_VISABASE_CONFIG
    And User clicks Pay button
    And User fills V2 authentication modal
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  @base_config @cardinal_commerce_v2.0
  Scenario: Support TransStatus I - MasterCard
    When User fills payment form with defined card MASTERCARD_SUPPORT_TRANS_STATUS_I
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color