# Created by user at 2/5/21
Feature: Verify that shopping cart is empty
  # Enter feature description here

  Scenario: Verify that shopping cart is empty
    Given Open Amazon page
    When Click on the cart icon
    Then Your Shopping Cart is empty