'''
Created on 2019-12-17
作者：蔡卓新
用途：学习V端-登录测试用例
'''

from selenium import webdriver
from common.BasePage import BasePage
from pages.Login_page import LoginPage
from common.read_excel import ExcelUtil
import os
import time
import unittest
import ddt

#测试数据
# testdata = [{"user":"admin","password":"admin"},
#             {"user":"测试11111","password":"测试322222"},
#             {"user":"00","password":"00"}]

#若获取当前执行脚本的绝对路径,再找父级、父级的父级
propath = (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#将获取的顶级目录名称与目标的文件夹、及下面的文件名进行拼接，形成完整路径
filepath = os.path.join(propath,'common','testdata.xlsx')
sheetName = 'Sheet1'
#实例化类对象
data = ExcelUtil(filepath,sheetName)
testdata = data.dict_data()

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
        url = 'http://66.3.17.180:8001/login.html'
        time.sleep(2)
        self.LoginPage = LoginPage(self.driver,url,'江苏·农村商业银行')
        self.driver.get('http://66.3.17.180:8001/login.html')
        # self.BP = BasePage(self.driver,'http://66.3.17.180:8001/login.html','江苏·农村商业银行')
        # self.BP.open()

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*testdata)
    def test_dtt(self,data):
        print('---开始进行测试---')
        self.login(data['user'],data['password'])
        print('测试数据：%s' %data)
        time.sleep(2)

        # EC.title_is
        # self.assertTrue()



if __name__ =="__main__":
    unittest.main()