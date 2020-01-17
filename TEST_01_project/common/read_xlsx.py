'''
Created on 2019-12-24
作者: 蔡卓新
用于读取excel文件数据2，重新写
'''
import xlrd
from selenium import webdriver
from time import sleep

def login(path):
    data = xlrd.open_workbook(path)    #打开excel表格，参数为文件路径
    sheet_names =  data.sheet_names() #获取所有sheet的名称
    table = data.sheet_by_name(sheet_names[0])  # 通过名称获取表格

    rows = table.nrows  #获取总行数

    for i in range(rows):   #获取每一行的数据
        row_content = table.row_values(i)
        username = row_content[0]
        password = int(row_content[1])   #读取的数字会变成float类型 如12345变为 12345.0
        return username,password

        # login_method(username, password) #传入账号和密码给selenium