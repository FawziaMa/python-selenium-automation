Feature: Sign In page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When User clicks Orders
    Then Verify Sign In page is opened


#  Scenario: Sign In from PopUp
#    Given Open Amazon page
#    When Click on button from SignIn PopUp
#    Then Sign in header and email input fields are visible
#

