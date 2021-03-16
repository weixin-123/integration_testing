#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : dev_use_sql.py
"""
from common.log_color import LogingColor

logging = LogingColor()
from common.connect_db import DoMysql


class UseSql:
    def recharge(self, phone):
        """
        充值业务
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id,account_id from life_member where username ='%s'" % phone
        sql_data = DoMysql().query_sql("member", sql)[0]
        # accountId = sql_data[0]
        # memberId = sql_data[1]
        return sql_data

if __name__ == "__main__":
    res = UseSql().recharge("13436182072")
    temp_res=res[0]
