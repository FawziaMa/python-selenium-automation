# Created by ledad at 10/5/2022
Feature: BestSellers page verification

  Scenario: User sees 5 links on BestSellers page
    When Open Amazon BestSellers page
    Then User sees 5 links on page

  Scenario: Verify correct page is opened under each header
    When Open Amazon BestSellers page
    Then Clicks on each top link and verifies that correct page opens
