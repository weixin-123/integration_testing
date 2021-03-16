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
    def query_merchant_id(self, phone):
        """
        通过username查询对应商家的id
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_car_merchants where member_username ='%s' and deleted_at is null and merchant_type = 1" % phone
        sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
        return sql_data


if __name__ == "__main__":
    data = UseSql().query_merchant_id(13436182072)
    print(data)
