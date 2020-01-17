'''
Created on 2019-12-17
作者：蔡卓新
用途：学习V端-登录页面，数据数据驱动
（用于测试多组数据检查）
关于ddt:
1 .测试数据为多个字典的list类型
2.测试类前加修饰@ddt.ddt
3.case前加修饰@ddt.data()
4.运行后用例会自动加载成三个单独的用例
'''

from selenium import webdriver
from common.BasePage import BasePage
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
import ddt

testdata = [{"user":"cctvmc43","password":"czx3311420"},
            {"user":"测试11111","password":"测试322222"},
            {"user":"00","password":"00"},]

@ddt.ddt
class login_case(unittest.TestCase):

    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')

    @ddt.data(*testdata)
    def test_dtt(self,data):
        print('---开始进行测试---')
        print(data)


if __name__ =="__main__":
    unittest.main()