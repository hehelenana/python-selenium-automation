Feature: Target website tests for HW4
Feature: Target website tests for HW4

  Scenario Outline: User can search for a product
    Given I open Target website for HW4
    When I search for "<product>" for HW4
    Then I should see search results for "<product>" for HW4

    Examples:
      | product |
      | coffee  |
      | candle  |

  Scenario: User can view Target Circle storycards
    Given I open Target Circle page for HW4
    Then I should see 2 storycards under Unlock added value for HW4

  Scenario: User can add a product to the cart
    Given I open Target website for HW4
    When I search for "coffee" for HW4
    And I add the first product to the cart for HW4
    Then I should see the product in the cart for HW4