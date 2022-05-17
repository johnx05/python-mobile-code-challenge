from appium.webdriver.common.mobileby import MobileBy
from features.support.screen_actions import ScreenActions


class CurrentConversionScreen():

    def __init__(self, driver):
        self.driver = driver

    def search_icon(self):
        self.driver.find_element(MobileBy.ID, 'action_search')

    def screen_title(self, title):
        self.driver.find_element(MobileBy.ID, 'action_bar')
        self.driver.find_element(MobileBy.XPATH, f"//android.widget.TextView[@text='{title}']")

    def from_unit(self):
        self.driver.find_element(MobileBy.ID,'from_units_spinner')
        self.driver.find_element(MobileBy.ID, 'select_unit_spinner')

    def to_unit(self):
        self.driver.find_elements(MobileBy.ID, 'select_unit_spinner')[1]

    # TODO: Implement a method to press keys in the app's keyboard
    # Step 1: Split the input string into each number
    # Step 2: Iterate through the array and find and click the number
    def press_keys(self, input_value):
        pass

    def read_result(self):
        self.driver.find_element(MobileBy.ID, 'target_value').text

    def click_fav_icon(self):
        self.driver.find_element(MobileBy.ID, 'action_add_favorites').click()

    def favorite_list_hint_values(self):
        all_favorites = self.driver.find_elements(MobileBy.ID, 'favorites_item_hint')
        return [favorite_values.text for favorite_values in all_favorites]

