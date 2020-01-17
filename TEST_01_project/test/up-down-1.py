from selenium import webdriver
import unittest
import time
from common.Base import Base
from pages.Version import Version_manage
'''导入PyUserInput模块中的PyKeyboard模块'''
import pymouse,pykeyboard,os,sys
from pykeyboard import PyKeyboard

from selenium.webdriver.support.ui import WebDriverWait

class login_test(unittest.TestCase):
    '''用户登录'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get('http://66.3.17.180:8001/login.html')
        self.base = Base(self.driver)
        self.ver = Version_manage(self.driver)


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        # self.driver.refresh() #重新刷新

    def test_001(self):
        '''模拟用户正常登录'''
        time.sleep(3)
        self.driver.find_element_by_id('loginUsername').send_keys('admin')
        self.driver.find_element_by_id('loginPassword').send_keys('admin')
        self.driver.find_element_by_name('forceLogin').click()
        self.driver.find_element_by_id('loginBtn').click()
        time.sleep(3)
        '''点击软件分发-版本管理'''
        self.driver.find_element_by_id("button-1124-btnWrap").click()
        self.driver.find_element_by_id("menuitem-1126-textEl").click()
        '''点击增加-选择JSNX'''
        self.driver.find_element_by_id("button-1291-btnEl").click()
        # '''JS清除只读，并写入版本类型，版本文件'''
        # self.ver.clear_ron_id('field_versionTypeComboBoxAdd-1303-inputEl')
        # self.base.sendkeys(("id", "field_versionTypeComboBoxAdd-1303-inputEl"),'JSNX_STM')
        time.sleep(3)
        '''JS点击版本类型'''
        self.ver.js_click_class("x-form-field x-form-empty-field x-form-required-field x-form-text x-trigger-noedit")
        self.ver.js_scroll_class_name("x-boundlist-list-ct x-unselectable","10000")
        '''点击JSNX-STM'''
        self.driver.find_element_by_css_selector(".x-boundlist-item:nth-of-type(10)").click()






        # self.driver.find_element_by_id("fileuploadfield-1304-button").click()
        # time.sleep(3)
        # K1 = pykeyboard.PyKeyboard()
        # # 切换英文输入
        # K1.tap_key(K1.shift_key)
        # K1.type_string('C:\gump2-increase-3.0.2.1-dist.rar')
        # time.sleep(2)
        # K1.tap_key(K1.enter_key)
        # time.sleep(2)
        # # 点击确认按钮
        # self.driver.find_element_by_id('button-1306-btnIconEl').click()
        # time.sleep(10)




if __name__ == '__main__':
    unittest.main()