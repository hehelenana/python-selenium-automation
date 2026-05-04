Feature: Target search and cart tests with Page Object Model for HW6

  Scenario: User can search for a product using Page Object Model
    Given Open Target main page for HW6
    When Search for coffee for HW6
    Then Verify search results for coffee shown for HW6

  Scenario: Your cart is empty message is shown for empty cart using Page Object Model
    Given Open Target main page for HW6
    When Click on Cart icon for HW6
    Then Verify empty cart message is shown for HW6


    