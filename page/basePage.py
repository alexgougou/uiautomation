from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):
    # 初始化
    def __init__(self, se_driver):
        self.driver = se_driver

    # 重写元素定位
    def find_element(self, *loc):
        # 确保元素是可见的。
        #  注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
        element = WebDriverWait(self.driver, 10, 0.5) \
            .until(EC.visibility_of_element_located(loc))
        return element

    # 重写send_keys方法
    def send_keys(self, loc, text):
        try:
            self.find_element(loc).clear()
            return self.find_element(loc).send_keys(text)
        except AttributeError:
            print("%s页面未能找到%s元素"(self, loc))

    # 重写click方法
    def click(self, *loc):
        return self.find_element(*loc).click()

    # 判断是否存在toast消息，存在返回true，不存在返回false
    def is_toast_exist(self, text):
        try:
            toast_loc = (By.XPATH, "//*[contains(@text, '%s')]" % text)
            WebDriverWait(self.driver, 10, 0.5).\
                until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            print(e)
            return False



