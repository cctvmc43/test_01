'''
created on 2019-12-12
作者：蔡卓新
pages\all_menu_user.py用于定位菜单栏元素及封装元素操作方法
'''

from common.BasePage import BasePage
from selenium.webdriver.common.by import By
# 继承BasePage类
class AllMenu(BasePage):
    # 定位器，通过元素属性定位元素对象
    rule_management_loc = (By.XPATH, '//*[@id="page-home"]/section/section/aside/div/div[1]/div/ul/li[8]/div')
    port_management_loc = (By.XPATH, '//*[@id="page-home"]/section/section/aside/div/div[1]/div/ul/li[8]/ul/li[2]')
    # 操作
    # 点击规则管理
    def click_rule_management(self):
        self.find_element(*self.rule_management_loc).click()
    # 点击端口管理
    def click_port_management(self):
        self.find_element(*self.port_management_loc).click()