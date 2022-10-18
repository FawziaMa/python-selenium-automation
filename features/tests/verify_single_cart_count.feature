Feature: Single item in cart

  Scenario: User has one item in cart
    Given Open Amazon page
    When Input lunch bags into search field
    And Click on search icon
    And "lunch bags" shown
    And Add item to cart
    Then Cart icon shows 1