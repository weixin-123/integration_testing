#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/08
@File    : test_use_sql.py
"""
from test_case.debt.check.test_sql import OnlineSql
from common.log_color import LogingColor

logging = LogingColor()
dev_db = OnlineSql()
begin_time = '2020-12-10 00:00:00'
end_time = '2020-12-11 00:00:00'


class DevDebtData:

    # 查询test：不同状态下的解债总数
    def query_contract(self, id):
        sql = "SELECT contract_id FROM  life_debt_order_apply where id  = '%s'" % id
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")

            return sql_data
        else:
            return sql_data



if __name__ == '__main__':
    # TestDebtData().query_test_orderid(14492075463)
    res = DevDebtData().query_contract(49)[0][0]
    print(res)
    # total = lencompleted_agent
    # print(total)



    # total = sql_data[0][0] + sql_data[0][1]
    # print(total)

