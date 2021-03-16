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
    def member_exists(self, phone):
        """
        是否是销巴会员
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select * from life_member where username = ('%s')" % phone
        sql_data = DoMysql().query_sql("member", sql)

        if sql_data == ():
            logging.info("%s不是销巴会员" % phone)
            return 'false'
        else:
            logging.info("%s是销巴会员，重新生成手机号" % phone)
            return 'true'


if __name__ == "__main__":
    # base_config.ini  更改数据库
    res = UseSql().member_exists("13436194260")
    temp_res=res[0]

