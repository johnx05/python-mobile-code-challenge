from behave import given, then, when
from features.screens.current_conversion_screen import CurrentConversionScreen
from features.screens.left_menu_screen import LeftMenuScreen
from features.android.config import driver

current_conversion_screen = CurrentConversionScreen(driver)
left_menu_screen = LeftMenuScreen(driver)


@given(u'I\'m on home screen')
def step_impl(context):
    current_conversion_screen.search_icon()
    current_conversion_screen.screen_title('Length')


@when(u'I click on the favorite icon')
def step_impl(context):
    current_conversion_screen.click_fav_icon()


@then(u"I see '{fav}' added to my favorites")
def step_impl(context, fav):
    favorite_conversions = current_conversion_screen.favorite_list_hint_values()
    print(f"favorites: {favorite_conversions}")
    assert fav in favorite_conversions


@when('I click (left|right) unit picker and select \'(.*)\'$/')
def step_impl(context, picker_type, unit_name):
    if picker_type == 'left':
        current_conversion_screen.from_unit.click()
        current_conversion_screen.scroll_and_click_unit(unit_name)
    elif picker_type == 'right':
        current_conversion_screen.to_unit.click()
        current_conversion_screen.scroll_and_click_unit(unit_name)


@when('I enter the number \'(.*)\' on app keyboard')
def step_impl(context, input_value):
    # |input|
    current_conversion_screen.press_keys(input_value)


@then('result is \'(.*)\'')
def step_impl(context, result):
    # |result|
    actual_result = current_conversion_screen.read_result()
    actual_result_trimmed = actual_result.delete(' ')
    assert actual_result_trimmed == result
