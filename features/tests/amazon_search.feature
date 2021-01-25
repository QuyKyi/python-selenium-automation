# Created by user at 1/25/21
Feature: Amazon Search
  # Enter feature description here

  Scenario: User can search for a produ
    Given Open Amazon age
    When Input Watches into Amazon search field
    And Click on Amazon search icon
    Then Product results for Watches are shown on Amazon