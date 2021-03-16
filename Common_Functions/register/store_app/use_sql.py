#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : dev_use_sql.py
"""
from common.log_color import LogingColor

logging = LogingColor()
from Common_Functions.database.dev_sql import DevSql


class UseSql:
    def query_member(self, phone):
        """
        查询会员member_id
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_member where username = ('%s')" % phone
        sql_data = DevSql().query_sql("member", sql)

        if sql_data == ():
            logging.info("%s不是销巴会员，请先注册销巴会员" % phone)
        else:
            logging.info("%s查询成功")
            return sql_data[0][0]

    def query_store_member(self, member_id):
        """
        通过order_id查询还款时间
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select * from store_stores where member_id = ('%s')" % member_id
        sql_data = DevSql().query_sql("store", sql)

        if sql_data == ():
            logging.info("你不是销巴商家，请先注册")
        else:
            logging.info("欢迎销巴商家，快去登录办业务吧！")

if __name__ == "__main__":
    data = UseSql().query_member(13436182072)
    print(data)
