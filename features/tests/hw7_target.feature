Feature: Target Sign In and cart tests with Page Object Model for HW7

  Scenario: Logged out user can access Sign In using Page Object Model
    Given Open Target main page for HW7
    When Click Account button for HW7
    And Click Sign In button from side navigation for HW7
    Then Verify Sign In form opened for HW7

  Scenario: User can add a product to the cart using Page Object Model
    Given Open Target main page for HW7
    When Search for coffee for HW7
    And Add first product to cart for HW7
    Then Verify product is in cart for HW7

    