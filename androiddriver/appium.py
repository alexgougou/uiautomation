from appium import webdriver


def setup_appium():
    caps = {"platformName": "ANDROID",
            "platformVersion": "8.1.0",
            "deviceName": "vivo Y85A",
            "app": "com.xueqiu.android",
            "noReset": True,
            "udid": "7bff6865",
            "appActivity": ".view.WelcomeActivityAlias "}
    driver_url = "http://172.21.12.105:4723/wd/hub"
    driver = webdriver.Remote(driver_url, caps)
    driver.implicitly_wait(5)
    return driver

