Feature: Mock for formId negative scenarios

  As a user
  I want to use card payments method with another formId
  In order to check negative scenarios

  Background:
    Given JavaScript configuration is set for scenario based on scenario's @config tag

  @form_id_config
  Scenario: Form id - decline payment
    Given AUTH response is set to "DECLINE"
    And THREEDQUERY mock response is set to "NOT_ENROLLED_U"
    When User opens prepared payment form page WITH_SPECIFIC_FORM_ID
    And User fills payment form with defined card VISA_CARD
    And User clicks Pay button
    Then User will see payment status information: "Decline"
    And User will see that notification frame has "red" color

  @form_id_config_visa_checkout
  Scenario: Form id - cancel payment with Visa checkout
    When User opens prepared payment form page WITH_SPECIFIC_FORM_ID
    And User chooses Visa Checkout as payment method - response is set to "CANCEL"
    Then User will see payment status information: "Payment has been cancelled"
    And User will see that notification frame has "yellow" color
    And VISA_CHECKOUT or AUTH requests were sent only once with correct data

  @form_id_config
  Scenario: Payment for form using different formId in config
    When User opens prepared payment form page WITH_CHANGED_FORM_ID
    Then User will see that application is not fully loaded