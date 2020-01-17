from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By
from selenium  import webdriver
from selenium import webdriver

class Base:

    def __init__(self,driver:webdriver.Chrome):
        #driver如果不加：webdriver.Firefox就是传的形参，加了就是映射了webdriver这个类，其他方法可以直接调用
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    # 重写元素定位方法 新加2020-1
    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def findelement_new(self, locator, timeout = 10, t = 0.5,):
        #定位到元素返回元素对象，没有定位到元素，返回timeout异常
        element = WebDriverWait(self.driver,timeout,t).until(exp.presence_of_element_located(locator))
        return element


    def findelement(self, locator, timeout = 10, t = 0.5,):
        # 抓取单个元素
        element = WebDriverWait(self.driver,timeout,t).until(lambda x: x.find_element(*locator))
        return element


    def findelements(self, loctor, timeout = 10, t = 0.5,):
        # 抓取一组元素
        try:
            elements = WebDriverWait(self.driver,timeout,t).until(lambda x: x.find_elements(*loctor))
            return elements
        except:
             return []


    def sendkeys(self,loctor,text,is_clear=False):
        # 找到元素并输入
        if is_clear:
            ele = self.findelement(loctor)
            ele.clear()
            ele.send_keys(text)
        # 转True的时候执行上面：
        else:
            ele = self.findelement(loctor)
            ele.send_keys(text)


    def click(self,loctor):
        # 找到元素并点击
        ele = self.findelement(loctor)
        ele.click()


    def clear(self,loctor):
        # 找到元素并清除
        ele = self.findelement(loctor)
        ele.clear()


    def isselected(self,loctor):
        # 找到元素判断是否为选中状态，包括多选框、radio、select下拉框等，返回bool值：true or false
        ele = self.findelement(loctor)
        r = ele.is_selected()
        return r



    def isdisplayed(self,loctor):
        # 判断元素是否存在，返回bool值：true or false
        ele = self.findelement(loctor)
        r = ele.is_displayed()
        return r


    def result(self,loctor):
        # 判断是否被全选中
        try:
            r = []
            all = self.findelements(loctor)
            for i in all:
                if not i.is_selected():
                    i.click()
                    r.append(i.is_selected())
                else:
                    r.append(i.is_selected())
            return r
        except:
            return False

    def is_title(self,_title,timeout = 10, t = 0.5):
        '''title中预期结果与实际传入driver是否相等'''
        try:
            result = WebDriverWait(self.driver, timeout, t).until(exp.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title,timeout = 10, t = 0.5):
        #title中预期结果是否包含driver实际结果的数据
        try:
            result = WebDriverWait(self.driver, timeout, t).until(exp.title_contains(_title))
            return result
        except:
            return False

    def text_in_to_element(self,locator,_text,timeout = 10, t = 0.5):
        try:
        #判断某个元素中的text是否包含了预期的字符串
            result = WebDriverWait(self.driver, timeout, t).until(exp.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def text_to_present_in_element_value(self,locator,_value,timeout = 10, t = 0.5):
        try:
        #判断某个元素中的value属性是否 包含了预期的字符串
        #返回bool值，values为空时，返回False
            result = WebDriverWait(self.driver, timeout, t).until(exp.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

        



# if __name__== "__mian__":
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get("http://66.16.17.180:8001/login.html")
#     findele = Base()
#     findele.sendkeys(("id","loginUsername"),"admin",True)
