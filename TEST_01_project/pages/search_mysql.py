'''
created on 2019-11-15
作者：蔡卓新
common\search_mysql.py用于封装查找数据库公共方法
'''

import pymysql
class SearchMysql():
    def search_mysql(self, sql):
        self.host = "*.*.*.*"
        self.user = "*"
        self.password = "*"
        self.database = "*"
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database, charset="utf8")
        self.cur = self.conn.cursor()
        self.sql1 = sql
        try:
            self.cur.execute(self.sql1)
            sth = self.cur.fetchall()[0][0]
        except:
            sth = '数据库未找到该数据！'
        return sth