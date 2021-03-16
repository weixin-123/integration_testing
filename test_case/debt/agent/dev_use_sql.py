#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/08
@File    : dev_use_sql.py
"""
from test_case.debt.admin_operation.dev_sql import CheckDevSql
from common.log_color import LogingColor

logging = LogingColor()
dev_db = CheckDevSql()
begin_time = '2020-12-10 00:00:00'
end_time = '2020-12-11 00:00:00'


class DevDebtData:
    # 查询dev：查询合同member_id
    def query_id(self, phone):
        sql = "SELECT id FROM life_member where username  = '%s'" % phone
        sql_data = dev_db.query_sql('member', sql)

        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return sql_data[0][0]
        else:
            return sql_data

    # 查询dev：查询合同id
    def query_contract(self, id):
        sql = "SELECT agent_contract_id,logo_contract_id,member_id FROM life_debt_agent where agent_id  = '%s'" % id
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return sql_data[0]
        else:
            return sql_data



if __name__ == '__main__':
    res=DevDebtData().query_id(13436187694)[0][0]
    print(res)
    # res = DevDebtData().query_contract(12)[0][2]
    # print(res)
    # total = lencompleted_agent
    # print(total)



    # total = sql_data[0][0] + sql_data[0][1]
    # print(total)

