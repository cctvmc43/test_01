
'''
Created on 2019-11-15

作者: 蔡卓新
testcases\zjtest_port.py用于编写创建端口组、编辑端口组、删除端口组用例
'''


import unittest
import time
from common.common_login import CommonLogin
from pages._7rule._2port.create_edit_port_page import CreateEditPortPage
from pages._7rule._2port.port_management_page import PortManagementPage
from pages.all_menu_user import AllMenu
from common.search_mysql import SearchMysql
class TestPort(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common_login = CommonLogin()
        cls.driver = cls.common_login.driver
        cls.url = cls.common_login.url
        cls.create_portname = "创建端口组"
        cls.create_portcontent = "80"
        cls.search_create_portname = "select name from gh_ports where name = " + '"'+ cls.create_portname + '"' +" and user_id = 83"
        cls.edit_portname = "编辑端口组"
        cls.edit_portname1 = "创建端口组编辑端口组"
        cls.edit_portcontent = ",8080"
        cls.search_edit_portname = "select name from gh_ports where name = " + '"'+ cls.edit_portname1 + '"' + " and user_id = 83"
        # 声明AllMenu、PortManagementPage、CreateEditPortPage、SearchMysql类对象
        cls.port_management_page = PortManagementPage(cls.driver, cls.url)
        cls.create_edit_port_page = CreateEditPortPage(cls.driver, cls.url)
        cls.all_menu = AllMenu(cls.driver, cls.url)
        cls.search_mysql = SearchMysql()
    # 新建端口组
    def test_1create_port(self):
        time.sleep(3)
        # 点击规则管理模块
        self.all_menu.click_rule_management()
        # 点击端口组管理模板模块
        self.all_menu.click_port_management()
        time.sleep(3)
        # 点击新建端口组按钮
        self.port_management_page.click_create_button()
        time.sleep(3)
        # 输入端口组名
        self.create_edit_port_page.input_port_name(self.create_portname)
        # 输入端口组内容
        self.create_edit_port_page.input_port_content(self.create_portcontent)
        # 点击确定按钮
        self.create_edit_port_page.click_confirm_button()
        time.sleep(3)
        self.assertEqual(self.port_management_page.get_text(), "添加成功", self.port_management_page.get_text())
        self.assertEqual(self.search_mysql.search_mysql(self.search_create_portname), self.create_portname, self.search_mysql.search_mysql(self.search_create_portname))
    # 编辑端口组
    def test_2edit_port(self):
        time.sleep(3)
        # 点击编辑端口组按钮
        self.port_management_page.click_edit_button()
        time.sleep(3)
        # 输入端口组名
        self.create_edit_port_page.input_port_name(self.edit_portname)
        # 输入端口组内容
        self.create_edit_port_page.input_port_content(self.edit_portcontent)
        # 点击确定按钮
        self.create_edit_port_page.click_confirm_button()
        time.sleep(3)
        self.assertEqual(self.port_management_page.get_text(), "保存成功", self.port_management_page.get_text())
        self.assertEqual(self.search_mysql.search_mysql(self.search_edit_portname), self.edit_portname1, self.search_mysql.search_mysql(self.search_edit_portname))
    # 删除端口组
    def test_3delete_port(self):
        time.sleep(3)
        # 点击删除端口组按钮
        self.port_management_page.click_delete_button()
        time.sleep(3)
        # 点击确定按钮
        self.port_management_page.click_confirm_button()
        time.sleep(3)
        self.assertEqual(self.port_management_page.get_text(), "删除成功", self.port_management_page.get_text())
        self.assertEqual(self.search_mysql.search_mysql(self.search_create_portname), '数据库未找到该数据！', "删除失败！")
        self.assertEqual(self.search_mysql.search_mysql(self.search_edit_portname), '数据库未找到该数据！', "删除失败！")
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()