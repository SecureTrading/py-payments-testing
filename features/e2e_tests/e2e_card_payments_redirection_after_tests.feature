Feature: E2E Card Payments - redirection
  As a user
  I want to be redirected to page matching my payment status
  So that my payment is handled appropriately

  @reactJS
  @e2e_config_submit_on_success
  Scenario: Successful payment with submitOnSuccess enabled
    Given JS library is configured with SUBMIT_ON_SUCCESS_CONFIG and BASE_JWT
    And User opens example page
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
    Given JS library is configured with REQUEST_TYPES_CONFIG and BASE_JWT
    And User opens example page
    When User fills payment form with defined card MASTERCARD_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |

  @reactJS
  @e2e_config_submit_on_error
  Scenario: Unsuccessful payment with submitOnError enabled
    Given JS library is configured with SUBMIT_ON_ERROR_CONFIG and BASE_JWT
    And User opens example page
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
    Given JS library is configured with SUBMIT_ON_SUCCESS_SECURITY_CODE_CONFIG and JWT_WITH_PARENT_TRANSACTION
    And User opens example page
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