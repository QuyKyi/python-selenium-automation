# Created by user at 2/5/21
Feature: Verify that add to cart
  # Enter feature description here

  Scenario: Verify that add to cart
    Given Open Amazon Product page
    When Press Add to Cart Button
    Then Verify that the Product is in Shopping Cart