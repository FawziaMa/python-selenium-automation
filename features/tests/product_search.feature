# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Shoes into search field
    And Click on search icon
    Then Product results for Shoes are shown

  Scenario: Verify search shows product name and image
    Given Open Amazon page
    When Input coffee into search field
    And Click on search icon
    Then Product results for coffee are shown


  Scenario:

