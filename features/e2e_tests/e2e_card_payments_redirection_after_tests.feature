Feature: E2E Card Payments - redirection
  As a user
  I want to be redirected to page matching my payment status
  So that my payment is handled appropriately

  Background:
    Given User opens page with payment form

  @e2e_config_submit_on_success
  Scenario: Successful payment with submitOnSuccess enabled
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |

  @e2e_config_request_types
  Scenario: Successful payment with requestTypes set and default submitOnSuccess
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |

  @e2e_config_submit_on_error
  Scenario: Unsuccessful payment with submitOnError enabled
    When User fills payment form with defined card MASTERCARD_DECLINED_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value   |
      | errormessage  | Decline |
      | baseamount    | 1000    |
      | currencyiso3a | GBP     |
      | errorcode     | 70000   |

  @e2e_config_submit_on_success_security_code
  Scenario: Successful payment with submitOnSuccess enabled with field to submit securitycode
    When User fills "SECURITY_CODE" field "123"
    And User clicks Pay button
    And User fills V1 authentication modal
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |