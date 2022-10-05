# Created by ledad at 9/24/2022
Feature: Amazon empty cart

  Scenario: User can verify empty cart
    Given Open Amazon page
    When User clicks cart icon
    Then User sees Your Amazon Cart is empty