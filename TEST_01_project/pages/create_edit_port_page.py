'''
created on 2019-12-12
作者：蔡卓新
pages\create_edit_port_page.py用于定位创建/编辑端口组界面元素及封装元素操作方法
'''



from common.BasePage import BasePage
from selenium.webdriver.common.by import By
# 继承BasePage类
class CreateEditPortPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    port_name_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input')
    port_content_loc = (By.CLASS_NAME, 'el-textarea__inner')
    confirm_button_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary')
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 输入端口组名
    def input_port_name(self, portname):
        self.find_element(*self.port_name_loc).send_keys(portname)
    # 输入端口组内容
    def input_port_content(self, portcontent):
        self.find_element(*self.port_content_loc).send_keys(portcontent)
    # 点击确定按钮
    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()