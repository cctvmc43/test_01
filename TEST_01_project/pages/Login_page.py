# coding=utf-8
'''
created on 2019-11-15
作者：蔡卓新
pages\login_page.py用于定位登陆页面元素，封装元素操作方法
'''

from common.BasePage import BasePage
from selenium.webdriver.common.by import By
# 继承BasePage类
class LoginPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.ID, 'loginUsername')
    password_loc = (By.ID, 'loginPassword')
    logincheckbox_loc = (By.NAME, "forceLogin")
    loginBt_loc = (By.ID, 'loginBtn')
    cancelBt_loc = (By.ID, 'cancelBtn')
    # submit_loc = (By.CSS_SELECTOR, '.login-text')
    # code_loc = (By.XPATH, '//*[@id="page-login"]/div[2]/form/div[3]/div/div/input')
    # loc1 = ("id", "loginUsername")
    # loc2 = ("id", "loginPassword")
    # loc3 = ("name", "forceLogin")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)
    # 输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)
    # 输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
    # 勾选强制登录框
    def click_logincheckbox(self):
        self.find_element(*self.logincheckbox_loc).click()
    # 点击登录
    def click_loginBt(self):
        self.find_element(*self.loginBt_loc).click()
    # 点击取消
    def click_cancelBt(self):
        self.find_element(*self.cancelBt_loc).click()

    # # 输入验证码
    # def input_code(self, code):
    #     self.find_element(*self.code_loc().send_keys(code)

