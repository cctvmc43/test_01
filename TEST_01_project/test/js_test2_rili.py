'''
created on 2019-12-27
作者：蔡卓新
学习使用JS操作日历，并输入日期
'''


#
# driver = webdriver.Firefox()
# driver.get('http://66.3.17.95:8001/index.jsp')
# driver.maximize_window()
# time.sleep(3)
# base = Base(driver)
#
# # user = 'document.getElementById("loginUsername").value = ("admin")'
# # Password = 'document.getElementById("loginPassword").value = ("admin")'
# # forceLogin = 'document.getElementsByName("forceLogin")[0].click()'
# # loginBtn = 'document.getElementById("loginBtn").click()'
# # # #执行JS脚本
# # # driver.execute_script(user)
# # # driver.execute_script(Password)
# # # driver.execute_script(forceLogin)
# # # driver.execute_script(loginBtn)
# time.sleep(3)
# driver.find_element_by_id('loginUsername').send_keys('admin')
# driver.find_element_by_id('loginPassword').send_keys('admin')
# driver.find_element_by_name('forceLogin').click()
# driver.find_element_by_id('loginBtn').click()
# time.sleep(3)
# driver.find_element_by_id("button-1092-btnWrap").click()
#
#
# # # base.click(("id","button-1092-btnIconEl"))
# # JS操作
# # jiankong = 'document.getElementById("button-1092-btnIconEl").click()'
# # driver.execute_script(jiankong)
#
#
#coding=utf-8
from selenium import webdriver
import unittest
import time
from common import Base
from selenium.webdriver.support.ui import WebDriverWait

class login_test(unittest.TestCase):
    '''用户登录'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get('http://66.3.17.180:8001/login.html')


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_001(self):
        '''模拟用户正常登录'''
        time.sleep(3)
        self.driver.find_element_by_id('loginUsername').send_keys('admin')
        self.driver.find_element_by_id('loginPassword').send_keys('admin')
        self.driver.find_element_by_name('forceLogin').click()
        self.driver.find_element_by_id('loginBtn').click()
        time.sleep(3)
        '''点击STM参数管理-STM参数操作日志'''
        self.driver.find_element_by_id("button-1219-btnWrap").click()
        self.driver.find_element_by_id("menuitem-1226-textEl").click()
        '''输入操作日期事件'''
        # JS去掉元素的readonly属性
        JS = 'document.getElementById("datetimefield-1240-inputEl").removeAttribute("readonly");'
        self.driver.execute_script(JS)
        # 清空输入框,并输入值
        self.driver.find_element_by_id("datetimefield-1240-inputEl").clear()
        self.driver.find_element_by_id("datetimefield-1240-inputEl").send_keys("2020-01-01")



if __name__ == '__main__':
    unittest.main()