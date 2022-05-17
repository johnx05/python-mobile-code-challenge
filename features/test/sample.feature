@sample
Feature: Unit Converter app challenge

  Background: Run this before each scenario
    Given I'm on home screen

  @fav
  Scenario: Add to favorite and verify it shows in Favorite conversions screen
    When I click on the menu icon
    # TODO: Implement scroll_and_click_unit method in screen_actions.rb to proceed
    And I click on 'Volume' menu item
    And I click on the favorite icon
    And I click on the menu icon
    And I scroll 'down' and click on 'Temperature' menu item
    And I click on the favorite icon
    When I click on the menu icon
    And I scroll 'up' and click on 'Favorite conversions' menu item
    # TODO: Implement conversions_list method in screen_actions.rb to proceed
    Then I see 'Volume' added to my favorites
    And I see 'Temperature' added to my favorites

  @select_left_picker
  Scenario: User is able to select values from left unit picker
    When I click left unit picker and select 'Meter'
    # TODO: Implement press_keys method in current_conversion_screen.rb to proceed
    And I enter the number '2' on app keyboard
    Then result is '200'

  @select_right_picker
  Scenario Outline: User is able to select values from right unit picker
    When I click on the menu icon
    And I click on 'Volume' menu item
    When I click right unit picker and select '<unit>'
    And I enter the number '<input>' on app keyboard
    Then result is '<result>'
    Examples:
      | unit           | input   | result    |
      | Hectoliter     | 564     | 21.3497   |
      | Drop, imperial | 0.05    | 1918.4813 |
