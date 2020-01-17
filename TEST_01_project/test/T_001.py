'''
Created on 2019-11-20
作者：蔡卓新
用途：学习调试
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class xuexi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        self.driver.find_element(By.ID,'kw').send_keys('aaa')
        result = EC.title_is('百度')
        print(result(self.driver))
        self.assertTrue(result(self.driver))

    def test_02(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys('aaa')
        result = EC.title_contains('百度')
        print(result(self.driver))
        self.assertTrue(result(self.driver))

if __name__ == '__main__':
    unittest.main()






