# Created by user at 1/25/21
Feature: Logged out user sees Sign in Page when clicking clicking
  # Enter feature description here

  Scenario: Logged out user sees Sign in Page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Sign in page opened