'''
created on 2019-12-14
作者：蔡卓新
用于定位V端监控-版本管理界面元素及封装元素操作方法
'''

from common.Base import Base


class Version_manage(Base):
    '''通过JS操作清除readonly属性（id类型）'''
    def js_clear_ronid_id(self,id):
        loc_ = id
        js = 'document.getElementById("{loc_ID}").removeAttribute("readonly");'.format(loc_ID=loc_)
        self.driver.execute_script(js)

    '''定义聚焦元素方法'''
    def js_focus_element(self, locator):
        # 聚焦元素
        target = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 具体的JS实现

    '''JS单击元素(id类型)'''
    def js_click_id(self,id):
        loc_ = id
        js = 'document.getElementById("{loc_ID}").click();'.format(loc_ID=loc_)
        self.driver.execute_script(js)

    '''JS单击元素(定位class类型)'''
    def js_click_class(self,class_name):
        loc_ = class_name
        js = 'document.getElementsByClassName("{loc_ID}")[0].click();'.format(loc_ID=loc_)
        self.driver.execute_script(js)

    '''JS内嵌纵向滚动（定位id类型）'''
    def js_scroll_id(self,id,value):
        loc_ = id
        value_ = value
        js = 'document.getElementById("{loc_ID}").scrollTop={value_ID};'.format(loc_ID=loc_, value_ID=value_)
        self.driver.execute_script(js)

    '''JS内嵌纵向滚动（定位class类型）'''
    def js_scroll_class_name(self,class_name,value):
        loc_ = class_name
        value_ = value
        js = 'document.getElementsByClassName("{loc_ID}")[0].scrollTop={value_ID};'.format(loc_ID=loc_, value_ID=value_)
        self.driver.execute_script(js)





if __name__ =="__main__":
    Version = Version_manage(Base)
    Version.clear_ron_id(111)
