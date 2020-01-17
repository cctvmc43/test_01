'''
Created on 2019-11-15

作者: 蔡卓新
common\common_login.py用于封装公共登陆方法，
其他测试用例有登陆操作直接调用该类中的方法即可完成登陆流程
'''

import unittest
import time
from pages.Login_page import LoginPage
from selenium import webdriver
class CommonLogin():
    # driver = webdriver.Chrome(executable_path=r"E:\TEST_01_project\driver\chromedriver.exe")
    # driver.implicitly_wait(30)
    # url = "http://66.3.17.180:8001/login.html"
    # username = "*"
    # password = "*"
    # code = "*"
    # # 声明LoginPage类对象
    login_page = LoginPage()
    # login_page = LoginPage(driver, url)
    # # 打开页面
    # login_page.open()
    # time.sleep(2)
    # 输入用户名
    login_page.input_username(username)
    # 输入密码
    login_page.input_password(password)
    # 勾选强制登录框
    login_page.click_logincheckbox()
    # 点击登录按钮
    login_page.click_loginBt()
    # 点击取消按钮
    login_page.click_cancelBt()
    # # 输入验证码
    # login_page.input_code(code)

if __name__ == "__main__":
    unittest.main()