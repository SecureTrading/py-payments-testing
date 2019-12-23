Feature: Behave Selenium Showcase

  Background:
    Given "payment_methods" page is open

  @sampleTest
  Scenario: Showing off behave and Selenium
    Then the title should contain "Secure Trading Example Form"