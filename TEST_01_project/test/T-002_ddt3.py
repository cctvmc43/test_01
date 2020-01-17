# coding:utf-8
import ddt
import time
import excelunit
import unittest
from selenium import webdriver

# 测试数据
data = excelunit.ExcelUtil("test.xlsx", "sheet1")
testData = data.dict_data()
print(testData)


@ddt.ddt
class Bolg(unittest.TestCase):
    """登录博客"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def login(self, username, psw):
        """登录方法,账号和密码参数化"""
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_sucess(self):
        """判断是否获取到登录账户名称"""
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print
            text
            return True
        except:
            return False

    @ddt.data(*testData)
    def test_login(self, data):
        """登录案例"""
        print("当前测试数据%s" % data)
        # 调用登录方法
        self.login(data["username"], data["password"])
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()