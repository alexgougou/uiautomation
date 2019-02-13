import unittest

from appium import webdriver
import time


class ShenmaTest(unittest.TestCase):
    def setUp(self):
        des_caps = {"platformName": "Android",
                    "deviceName": "2a0c466c",
                    "appPackage": "com.shenma.passenger",
                    "noReset": True,
                    "resetKeyboard": True,
                    "autoGrantPermissions": True,
                    "unicodeKeyboard": True,
                    "appActivity": ".ui.activity.SplashActivity"}
        driver_url = "http://127.0.0.1:4723/wd/hub"
        self.driver = webdriver.Remote(driver_url, des_caps)
        self.driver.implicitly_wait(10)

    def test_h5(self):
        time.sleep(10)
        el = "android.widget.ImageView"
        if el in self.driver.page_source:
            self.driver.back()

        self.driver.find_element_by_id("left_icon").click()

    def tearDown(self):
        self.driver.quit()
