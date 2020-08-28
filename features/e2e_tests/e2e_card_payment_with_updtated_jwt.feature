Feature: E2E Card Payments with updated jwt

  As a user
  I want to use card payments method
  In order to check full payment functionality with updated jwt

  @reactJS
  @angular
  Scenario: Successful payment with updated jwt
    Given JS library is configured with DEFER_INIT_CONFIG and BASE_JWT
    And User opens example page WITH_UPDATE_JWT
      | jwtName          |
      | BASE_UPDATED_JWT |
    When User calls updateJWT function by filling amount field
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  Scenario: Successful payment with updated jwt and without locale param
    Given JS library is configured with DEFER_INIT_CONFIG and JWT_WITHOUT_LOCALE
    And User opens example page WITH_UPDATE_JWT
      | jwtName                                            |
      | JWT_WITHOUT_LOCALE_AND_UPDATED_AMOUNT_AND_CURRENCY |
    When User calls updateJWT function by filling amount field
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will see payment status information: "Payment has been successfully processed"
    And User will see that notification frame has "green" color

  #just to make sure data are taken from updated jwt
  @reactJS
  @angular
  @update_jwt_test
  Scenario: Successful payment with updated jwt without locale param and submit on success config
    Given JS library is configured with DEFER_INIT_AND_SUBMIT_ON_SUCCESS_CONFIG and JWT_WITHOUT_LOCALE
    And User opens example page WITH_UPDATE_JWT
      | jwtName                                            |
      | JWT_WITHOUT_LOCALE_AND_UPDATED_AMOUNT_AND_CURRENCY |
    When User calls updateJWT function by filling amount field
    And User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 2000                                    |
      | currencyiso3a | EUR                                     |
      | errorcode     | 0                                       |