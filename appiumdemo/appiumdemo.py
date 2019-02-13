from appium import webdriver

caps = {"platformName": "Android",
        "deviceName": "2a0c466c",
        "appPackage": "com.xueqiu.android",
        "noReset": True,
        "resetKeyboard": True,
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "appActivity": ".view.WelcomeActivityAlias "}

driver_url: str = "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(driver_url, caps)
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@text='自选']").click
driver.quit()
