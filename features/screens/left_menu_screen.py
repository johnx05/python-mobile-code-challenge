from appium.webdriver.common.mobileby import MobileBy
from features.support.screen_actions import ScreenActions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class LeftMenuScreen():
    def __init__(self, driver):
        self.driver = driver
        self.actions = TouchAction(driver)

    def click_menu(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Open navigation drawer").click()

    def select_menu_option(self, menu_option):
        search_param = f"//android.widget.TextView[@text='{menu_option}']"
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
            (MobileBy.XPATH, search_param)
        )).click()

    def left_menu_displayed(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Close navigation drawer")
        self.driver.find_element(MobileBy.ID, "categories_drawer_layout")
        self.driver.find_element(MobileBy.ID, "drawerItem")

    def scroll_to_option_and_click(self, option_value, direction='down'):
        if direction == 'down':
            last_value = 'Astronomy distance'
            first_index = 0
            last_index = -1
        else:
            last_value = 'Favorite conversions'
            first_index = -1
            last_index = 0

        while True:
            try:
                self.select_menu_option(option_value)
                return
            except TimeoutException:
                all_menu_options = self.driver.find_elements(MobileBy.ID, "drawerCategoryName")
                last_menu_option_value = all_menu_options[last_index]
                first_menu_option_value = all_menu_options[first_index]
                element_distance = -1 * (last_menu_option_value.location['y'] - first_menu_option_value.location['y']) / 2
                self.actions.press(last_menu_option_value).wait(800).move_to(x=last_menu_option_value.location['x'],
                           y=element_distance).release().perform()
            if last_menu_option_value.text == last_value:
                break
        raise NoSuchElementException(f"Menu option {option_value} was not be found")




