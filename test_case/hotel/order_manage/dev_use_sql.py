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

    # 查询hd：查询酒店房间信息
    def query_hotel_detail(self, hotel_id, order_id):
        sql = "SELECT room_id,room_name,bed FROM  order_room_info where hotel_id = '%s' and id = %s" % (hotel_id, order_id)
        sql_data = dev_db.query_sql('hotel', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return sql_data
        else:
            return sql_data

    # # 查询hd：查询会员信息
    # def query_member_detail(self, telephone):
    #     sql = "SELECT room_name,bed FROM  order_room_info where username = '%s' " % (telephone)
    #     sql_data = dev_db.query_sql('hotel', sql)
    #     if sql_data == "" or sql_data is None:
    #         logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
    #         return sql_data[0]
    #     else:
    #         return sql_data


if __name__ == '__main__':
    # TestDebtData().query_test_orderid(14492075463)
    res = DevDebtData().query_hotel_detail(776692, 2)[0][1]
    print(res)
    # total = lencompleted_agent
    # print(total)



    # total = sql_data[0][0] + sql_data[0][1]
    # print(total)

