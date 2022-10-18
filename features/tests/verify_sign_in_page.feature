Feature: Sign In page
  Scenario: User sees sign in header and email input fields
    Given Open Amazon page
    When User clicks Orders
    Then Sign in header and email input fields are visible


  Scenario: Sign In from PopUp
    Given Open Amazon page
    When Click on button from SignIn PopUp
    Then Verify Sign in page opened
