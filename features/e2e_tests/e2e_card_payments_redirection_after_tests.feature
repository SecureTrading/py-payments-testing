Feature: E2E Card Payments - redirection
  As a user
  I want to be redirected to page matching my payment status
  So that my payment is handled appropriately

  @reactJS
  @angular
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
  @angular
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

  @reactJS
  @angular
  @e2e_config_submit_on_error_invalid_jwt
  Scenario: Unsuccessful payment with submitOnError enabled
    Given JS library is configured with SUBMIT_ON_ERROR_CONFIG and INVALID_JWT
    And User opens example page
    Then User will not see notification frame
    And User will be sent to page with url "www.example.com" having params
      | key          | value         |
      | errormessage | Invalid field |
      | errorcode    | 30000         |
      | errordata    | locale        |


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

  @e2e_config_submit_on_success_callback
  Scenario: Successful payment with submitOnSuccess enabled and success callback set
    Given JS library is configured with SUBMIT_ON_SUCCESS_CONFIG_SUCCESS_CALLBACK and BASE_JWT
    When User opens example page SUCCESS_CALLBACK
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "example.org" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |

  @reactJS
  @angular
  @e2e_config_submit_on_success_callback_submit
  Scenario: Successful payment with submitOnSuccess enabled and submit callback set
    Given JS library is configured with SUBMIT_ON_SUCCESS_CONFIG_SUBMIT_CALLBACK and BASE_JWT
    When User opens example page SUBMIT_CALLBACK
    When User fills payment form with defined card VISA_FRICTIONLESS
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "example.org" having params
      | key           | value                                   |
      | errormessage  | Payment has been successfully processed |
      | baseamount    | 1000                                    |
      | currencyiso3a | GBP                                     |
      | errorcode     | 0                                       |

  @reactJS
  @angular
  @e2e_config_submit_on_error_callback
  Scenario: Unsuccessful payment with submitOnError enabled and error callback set
    Given JS library is configured with SUBMIT_ON_ERROR_CONFIG_ERROR_CALLBACK and BASE_JWT
    When User opens example page ERROR_CALLBACK
    When User fills payment form with defined card VISA_DECLINED_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "example.org" having params
      | key           | value   |
      | errormessage  | Decline |
      | baseamount    | 1000    |
      | currencyiso3a | GBP     |
      | errorcode     | 70000   |

  @e2e_config_submit_on_error_callback
  Scenario: Unsuccessful payment with submitOnError enabled and submit callback set
    Given JS library is configured with SUBMIT_ON_ERROR_CONFIG_SUBMIT_CALLBACK and BASE_JWT
    When User opens example page SUBMIT_CALLBACK
    When User fills payment form with defined card VISA_DECLINED_CARD
    And User clicks Pay button
    Then User will not see notification frame
    And User will be sent to page with url "example.org" having params
      | key           | value   |
      | errormessage  | Decline |
      | baseamount    | 1000    |
      | currencyiso3a | GBP     |
      | errorcode     | 70000   |

  @e2e_config_submit_on_cancel_callback
  Scenario: Unsuccessful payment with submitOnCancel enabled and cancel callback set
    Given JS library is configured with SUBMIT_ON_CANCEL_CONFIG_CANCEL_CALLBACK and BASE_JWT
    When User opens example page CANCEL_CALLBACK
    And User clicks on Visa Checkout button
    And User closes the visa checkout popup
    Then User will not see notification frame
    And User will be sent to page with url "example.org" having params
      | key          | value                      |
      | errormessage | Payment has been cancelled |
      | errorcode    | cancelled                  |