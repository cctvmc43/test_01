'''
created on 2019-11-15
作者：蔡卓新
pages\port_management_page.py用于定位端口管理界面元素及封装元素操作方法
'''

from common.BasePage import BasePage
from selenium.webdriver.common.by import By
# 继承BasePage类
class PortManagementPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    create_button_loc = (By.XPATH, '//*[@id="page-home"]/section/section/main/div[2]/div[1]/div/div/button')
    edit_button_loc = (By.XPATH, '//*[@id="page-home"]/section/section/main/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]')
    delete_button_loc = (By.XPATH, '//*[@id="page-home"]/section/section/main/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]')
    confirm_button_loc = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')
    text_loc = (By.CLASS_NAME, 'el-message__content')
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 点击新建按钮
    def click_create_button(self):
        self.find_element(*self.create_button_loc).click()
    # 点击编辑按钮
    def click_edit_button(self):
        self.find_element(*self.edit_button_loc).click()
    # 点击删除按钮
    def click_delete_button(self):
        self.find_element(*self.delete_button_loc).click()
    # 点击弹出框确定按钮
    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()
    # 获取提示信息
    def get_text(self):
        try:
            text =  self.find_element(*self.text_loc).text
        except:
            text = "未获取到提示信息！"
        return text