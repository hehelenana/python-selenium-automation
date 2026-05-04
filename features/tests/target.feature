Feature: Target website navigation for HW3

  Scenario: User can open empty cart
    Given I open Target website for HW3
    When I click the cart icon for HW3
    Then I should see the empty cart message for HW3

  Scenario: Logged out user can access Sign In
    Given I open Target website for HW3
    When I click the account button for HW3
    And I click sign in from the side menu for HW3
    Then I should see the sign in form for HW3