Feature: User Login

  Scenario: Successful Login
    Given I am on the login page
    When I enter valid credentials
    Then I should be logged in successfully
