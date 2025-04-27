Feature: Login functionality

  @IPC_LOGIN_001
  Scenario: Successful login with correct credentials
    Given a registered user
    When the user logs in with valid credentials
    Then access is granted
