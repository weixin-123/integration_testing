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

    def query_store_member(self, phone):
        """
        判断是否是销巴会员 如果是返回的结果不为空 反之
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select * from store_stores where member_id = ('%s')" % phone
        sql_data = DoMysql().query_sql("store", sql)
        if sql_data == ():
            logging.info("%s不是销巴会员" % phone)
        else:
            logging.info("%s是销巴会员，重新生成手机号" % phone)
            return 'true'


if __name__ == "__main__":
    data = UseSql().query_store_member(13436185246)
    print(data)
