# Created by user at 1/25/21
Feature: Amazon Search
  # Enter feature description here

  Scenario Outline: User can search for Watches
    Given Open Amazon page
    When Input <search_query> into Amazon search field
    And Click on Amazon search icon
    Then Product results for <result> are shown on Amazon
    And Page URL has <search_query> in it
    Examples:
      |search_query| result|
      |Watches     |"Watches"|
      |Dress       |"Dress"  |


  Scenario: User can search for a Dress
    Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then Product results for "Dress" are shown on Amazon
    And Page URL has Dress in it