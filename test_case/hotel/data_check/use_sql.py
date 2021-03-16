#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : dev_use_sql.py
"""
import json

from common.log_color import LogingColor

logging = LogingColor()
from common.connect_db import DoMysql


class UseSql:
    def que_city(self, city_name):
        """
        查询城市下面的省份
        """
        logging.info("----------查询数据库----------")
        sql = "select peripheral from peripheral where city_name = ('%s') " % city_name
        sql_data = DoMysql().query_sql("hotel", sql)
        if sql_data == ():
            logging.info("查询失败")
            return 'true'
        else:
            logging.info("查询成功，%s下面的省市如下：" % city_name)
            return sql_data[0][0]


# [0]['area']['pros']['poi_list']
if __name__ == "__main__":
    res = UseSql().que_city("重庆")
    res_1 = list(res)
    tuple_now = tuple(res_1)
    print(type(tuple_now))
    print(tuple_now)
