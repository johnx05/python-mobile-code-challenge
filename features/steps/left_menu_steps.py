from behave import given, then, when
from features.screens.current_conversion_screen import CurrentConversionScreen
from features.screens.left_menu_screen import LeftMenuScreen
from features.android.config import driver


current_conversion_screen = CurrentConversionScreen(driver)
left_menu_screen = LeftMenuScreen(driver)


@when("I click on the menu icon")
def step_impl(context):
    left_menu_screen.click_menu()
    left_menu_screen.left_menu_displayed()


@when("I click on '{menu_item}' menu item")
def step_impl(context, menu_item):
    print(f"variable value: {menu_item}")
    left_menu_screen.select_menu_option(menu_item)
    current_conversion_screen.screen_title(menu_item)


@when("I scroll '{direction}' and click on '{menu_item}' menu item")
def step_impl(context, direction, menu_item):
    left_menu_screen.scroll_to_option_and_click(menu_item, direction)
