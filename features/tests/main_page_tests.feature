# Created by white at 3/20/2024
Feature: Main page tests

  Scenario: User can open the main page and verify it has a map
    Given Open the main page
    When Scroll down to the footer
    And Verify the title Cafedaria in the footer exists
    Then Verify the footer contains a map


  Scenario: User can see and click on the elements in the navigation bar
    Given Open the main page
    When Verify the title Cafedaria exists on the navigation bar
    And Verify there are 6 sub-titles in the navigation bar and all of them are clickable
    Then Verify the cart and search icons exists