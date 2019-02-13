import unittest
from appium import webdriver

from page.mainPage import MainPage


class TestUserCenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desire_caps = {"platformName": "Android",
                       "deviceName": "2a0c466c",
                       "appPackage": "com.shenma.passenger",
                       "noReset": True,
                       "resetKeyboard": True,
                       "autoGrantPermissions": True,
                       "unicodeKeyboard": True,
                       "appActivity": ".ui.activity.SplashActivity"
                       }
        remote_url = "http://127.0.0.1:4723/wd/hub"
        cls.driver = webdriver.Remote(remote_url, desire_caps)
        cls.driver.implicitly_wait(10)
        cls.mainPage = MainPage(cls.driver)

    def test_user_center(self):
        self.mainPage.go_user_center()

    def test_demo2(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
