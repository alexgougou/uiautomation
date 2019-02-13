from appium import webdriver


class Driver:
    def __init__(self):
        caps = {"platformName": "ANDROID",
                "platformVersion": "8.1.0",
                "deviceName": "vivo Y85A",
                "app": "com.xueqiu.android",
                "noReset": True,
                "udid": "7bff6865",
                "appActivity": ".view.WelcomeActivityAlias "}
        self.driver_url = "http://172.21.12.105:4723/wd/hub"
        self.driver = webdriver.Remote(self.driver_url, caps)
        self.driver.implicitly_wait(5)
        return self.driver

