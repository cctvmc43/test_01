'''
Created on 2019-12-17
作者：蔡卓新
用途：学习V端-登录页面，数据数据驱动
（用于测试多组数据检查）
'''

from selenium import webdriver
# from common.BasePage import BasePage
from pages.Login_page import LoginPage
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
import ddt

testdata = [{"user":"admin","password":"admin"},
            {"user":"测试11111","password":"测试322222"},
            {"user":"00","password":"00"}]

@ddt.ddt
class login_case(unittest.TestCase):

    # def login(self, username, password):
    #     self.BP.send_keys(loc1,username)
    #     self.BP.send_keys(loc2,password)
    #     # self.BP.find_element(loc3)
    #     self.driver.find_element_by_name('forceLogin').click()
    #     self.driver.find_element_by_id('loginBtn').click()
    def login(self, username, password):
        self.LoginPage.input_username(username)
        self.LoginPage.input_password(password)
        self.LoginPage.click_logincheckbox()
        self.LoginPage.loginBt_loc()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.LoginPage = LoginPage(BasePage)
        self.LoginPage.open('http://66.3.17.180:8001/login.html','江苏·农村商业银行')

        # self.BP = BasePage(self.driver,'http://66.3.17.180:8001/login.html','江苏·农村商业银行')
        # self.BP.open()

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*testdata)
    def test_dtt(self,data):
        print('---开始进行测试---')
        self.login(data['user'],data['password'])
        print('测试数据：%s' %data)

        # EC.title_is
        # self.assertTrue()



if __name__ =="__main__":
    unittest.main()