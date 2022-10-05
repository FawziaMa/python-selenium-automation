# Created by ledad at 10/5/2022
Feature: BestSells links count

  Scenario: User sees 5 links on BestSellers page
    When Open Amazon BestSellers page
    Then User sees 5 links on page
