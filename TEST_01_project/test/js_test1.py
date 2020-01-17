'''
created on 2019-12-26
作者：蔡卓新
学习使用JS进行滚动聚焦元素
'''
from selenium import webdriver
import time
from pages.Login_page import LoginPage


driver = webdriver.Firefox()
driver.get('https://www.cnblogs.com/ooo0/p/7742214.html')
driver.maximize_window()
time.sleep(3)
target = driver.find_element_by_id('green_channel_follow')
#具体滚动聚焦元素方法学习
driver.execute_script("arguments[0].scrollIntoView();", target)
target.click()
