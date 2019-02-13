from selenium.webdriver.common.by import By
from appium import webdriver

from page.basePage import BasePage
from page.h5Page import H5Page
from page.usercenterPage import UserCenterPage


class MainPage(BasePage):
    h5locator = (By.ID, "ll_store_visitor")
    user_center = (By.ID, 'left_icon')
    my_trip = (By.ID, "tv_trip")

    def go_h5(self):
        self.find_element(*self.h5locator).click()
        return H5Page(self.driver)

    def go_user_center(self):
        # self.find_element(10, 0.5, *self.user_center).click()
        self.click(*self.user_center)
        # return UserCenterPage(self.driver)

    def go_my_trip(self):
        self.click(*self.my_trip)

