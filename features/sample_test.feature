Feature: Behave Selenium Showcase

  Background:
    Given "Sample" page is open

  @sampleTest
  Scenario: Showing off behave and Selenium
    Then the title should contain "Google"
    And mock json should be visible on specific url