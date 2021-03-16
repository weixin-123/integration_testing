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
end_time = '2020-12-12 00:00:00'


class DevDebtData:

    # 查询test：不同状态下的解债总数
    def query_dev_count(self,status):
        sql = "SELECT count(id) FROM `life_debt_order_apply` where status in ('%s') and created_at between '%s' and '%s'" % (status, begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data[0][0]

    # 查询test：随机获取一个债务人手机号
    def query_dev_debtor_mobile(self):
        sql = "SELECT debtor_mobile FROM life_debt_order_apply t1 JOIN" \
              " (SELECT RAND() * (SELECT MAX(id) FROM life_debt_order_apply) AS nid) t2 ON t1.id > t2.nid LIMIT 1"
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data[0][0]

    # 查询test：获取债务人的订单号
    def query_dev_orderid(self, phone):
        sql = "SELECT id FROM life_debt_order_apply where debtor_mobile = '%s' " % phone
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data[0][0]

    # 查询test：获取订单id
    def query_dev_order_id(self):
        sql = "SELECT distinct order_id  FROM life_debt_order_list"
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data

    # 查询单人待还债权微币
    def completing_coins(self, order_id):
        sql = "SELECT repayment_amount_sum,number_periods FROM life_debt_order_list where order_id = '%s' and state = 2  order by number_periods desc" % order_id
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有待还债权微币")
        else:
            return sql_data[0][0]

    # 查询单人已还债权微币
    def completed_coins(self, order_id):
        sql = "SELECT count(number_periods),money FROM life_debt_order_list where order_id = '%s' and state != 2" % order_id
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有已还债权微币")
        else:
            print(sql_data)
            return sql_data[0]

    # # 查询test：通过电话号码随机获取一个订单号
    # def query_test_ordersn(self, phone):
    #     sql = "SELECT order_sn FROM life_debt_order_apply where debtor_mobile = '%s'" % phone
    #     sql_data = test_db.query_sql('debt', sql)
    #     if sql_data == "" or sql_data is None:
    #         logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
    #         return "False"
    #     else:
    #         newStr = ''.join(list(filter(str.isdigit, sql_data[0][0])))
    #         print(newStr)
    #         return newStr

    # 查询test：指定用户的解债情况
    # number_periods 还款期数 money 每月还款金额 repayment_amount_sum 待还款总额 state 还款状态 （1.待还  2. 已还 3.冻结）
    def query_dev_agent_detail(self, order_id, state):
        sql = "SELECT number_periods, money, repayment_amount_sum, state FROM life_debt_order_list " \
              "where order_id  = '%s' and state = '%s' order by number_periods desc" % (order_id, state)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有需要解债的")
        else:
            return sql_data

        # 查询test：指定用户的解债情况
        # number_periods 还款期数 money 每月还款金额 repayment_amount_sum 待还款总额 state 还款状态 （1.待还  2. 已还 3.冻结）


    def query_dev_all_agent_detail(self, state):
        sql = "SELECT number_periods, money, repayment_amount_sum FROM life_debt_order_list where state = '%s' and created_at between '%s' and '%s'" % (state, begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有需要解债的")
        else:
            return sql_data

    # 已完成解债金额  60 130
    def completed_debt_cash(self):
        sql = "SELECT amount,interest_amount FROM life_debt_order_apply where status in (60,130) and created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有已完成的解债信息")
        else:
            print(sql_data[0][0])
            return sql_data

    # 已完成解债金额  60 130
    def completing_debt_cash(self):
        sql = "SELECT amount,interest_amount FROM life_debt_order_apply where status not in (60,130) and created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有已完成的解债金额")
        else:
            print(sql_data[0][0])
            return sql_data

    # 已完成解债金额笔数
    def completed_debt_cash_total(self):
        sql = "SELECT count(id) FROM life_debt_order_apply where status not in (60,130) and created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有已完成的解债数")
        else:
            print(sql_data[0][0])
            return sql_data

    # 债务人需偿还债务金额
    def completed_debtor(self):
        sql = "SELECT amount,interest_amount,reduction_amount FROM life_debt_order_apply where created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有需偿还的的解债金额")
        else:
            print(sql_data[0][0])
            return sql_data

    # 已结算经纪人劳务费
    def completed_agent(self):
        sql = "SELECT agent_profit FROM life_debt_order_apply where status in (60,130) and created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('debt', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == ():
            logging.error("没有已结算经纪人劳务费")
        else:
            print(sql_data[0][0])
            return sql_data





if __name__ == '__main__':
    # TestDebtData().query_test_orderid(14492075463)
    sql_data = DevDebtData().query_dev_all_agent_detail()
    # total = lencompleted_agent
    # print(total)



    # total = sql_data[0][0] + sql_data[0][1]
    # print(total)

