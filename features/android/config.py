from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, "PreciseUnitConversion.apk")
APPIUM = 'http://localhost:4723/wd/hub'

CAPS = {
            "deviceName": "pixel_2",
            "platformName": "Android",
            "platformVersion": "11",
            "automationName": "UiAutomator2",
            "app": APP,
            "appPackage": "com.ba.universalconverter",
            "appActivity": "MainConverterActivity",
            "new-command-timeout": "3600"
      }

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)