# Created by Svetlana at 4/4/19
Feature: Deals Search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Shoes into search field
    And Click on search icon
    Then Product results for Shoes are shown

  Scenario: Verify search shows product name and image
    Given Open Amazon page
    When Input coffee into search field
    And Click on search icon
    Then Verify image and product name


  Scenario: User can view new deals on product's page
    Given Open B074TBCSC8 deal page
    When User hovers over New Arrivals
    Then Verify deals are shown


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by value electronics
    And Input AirPods into search field
    And Click on search icon
    Then Verify electronics department is selected