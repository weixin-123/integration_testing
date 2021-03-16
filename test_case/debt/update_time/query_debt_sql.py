#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
<<<<<<< HEAD
@File    : dev_use_sql.py
"""
from test_case.debt.admin_operation.dev_sql import CheckDevSql
from common.log_color import LogingColor

logging = LogingColor()
dev_db = CheckDevSql()
=======
@File    : test_use_sql.py
"""
from test_case.debt.check.test_sql import OnlineSql
from common.log_color import LogingColor

logging = LogingColor()
dev_db = OnlineSql()
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587

class UseSql:

    def use_sql_select_order(self, order_id):
        """
        通过order_id查询还款时间
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select repayment_time from life_debt_order_list where order_id = '%s' and number_periods = 36" % order_id
        sql_data = dev_db .query_sql("debt", sql)
        if sql_data == ():
            logging.info("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return 'false'
        else:
            return sql_data[0][0]

    def use_sql_execute_time(self, order_id, time):
        """
        通过order_id查询还款时间
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "update life_debt_order_list set repayment_time = '%s' where order_id = '%s' and number_periods = 36" % (time, order_id)
        sql_data = dev_db .execute_sql("debt", sql)
        if sql_data == ():
            logging.info("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return 'false'
        else:
            return sql_data


if __name__ == "__main__":
    data = UseSql().use_sql_execute_time(54,)
    print(data)
    # temp_data = data.strftime("%Y-%m-%d")
    # print(temp_data)
