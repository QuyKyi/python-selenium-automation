# Created by user at 2/5/21
Feature: Cancelling an order on Amazon
  # Enter feature description here

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel order into Amazon Search Help Library field
    Then Cancel Items or Orders text is present