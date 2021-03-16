#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/08
@File    : data_fractionation.py
"""
from test_case.debt.data_check.dev_use_sql import DevDebtData

# phone = DevDebtData().query_dev_debtor_mobile()
# print('phone:', phone)
phone = 13300000001


class DataFractionation:
    # # 单人待还债权微币
    # def dav_to_be_completed(self):
    #     order_id = DevDebtData().query_dev_orderid(phone)
    #     print('order_id:', order_id)
    #     sql_data = DevDebtData().query_dev_agent_detail(order_id, 1)
    #     return sql_data

    # 总代还债权微币
    def dev_all_to_be_completing(self):
        pay_datas = DevDebtData().query_dev_all_agent_detail(1)
        sum = 0
        for i in pay_datas:
            # print("i的值为：", i)
            periods = i[0]
            repayment_quota = i[1]
            # print("期数：",periods)
            # print("每月还款额度：", repayment_quota)
            all_quota = 36 - (periods - 1) * repayment_quota
            # print("待还款微币为：", all_quota)
            sum = sum + all_quota
        # 取绝对值
        # print(abs(sum))
        return abs(sum)

    # 单人已还债权微币
    # def dav_completed(self):
    #     order_id = DevDebtData().query_dev_orderid(phone)
    #     print('order_id:', order_id)
    #     sql_data = DevDebtData().query_dev_agent_detail(order_id, 2)
    #     return sql_data

    # 总已还债权微币
    def dev_all_to_be_completed(self):
        pay_datas = DevDebtData().query_dev_all_agent_detail(2)
        sum = 0
        for i in pay_datas:
            completed_cash = i[2]
            sum = sum + completed_cash
        # print(sum)
        return sum

    # 已完成解债金额
    def dev_cash_completed_first_step(self):
        sql_data = DevDebtData().completed_debt_cash()
        total = len(sql_data)
        temp_list = []
        for i in range(total):
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            data = sql_data[i][0] + sql_data[i][1]
            temp_list.append(data)
        return temp_list

    def dev_cash_complete_second_step(self):
        cash_data = DataFractionation().dev_cash_completed_first_step()
        print(cash_data)
        sum = 0
        for i in cash_data:
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            sum = i+sum
        print(sum)
        return sum


    # 待完成解债金额
    def dev_cash_completing_first_step(self):
        sql_data = DevDebtData().completing_debt_cash()
        total = len(sql_data)
        temp_list = []
        for i in range(total):
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            data = sql_data[i][0] + sql_data[i][1]
            temp_list.append(data)
        return temp_list

    def dev_cash_completing_second_step(self):
        cash_data = DataFractionation().dev_cash_completing_first_step()
        print(cash_data)
        sum = 0
        for i in cash_data:
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            sum = i + sum
        print(sum)
        return sum

    # 已收需偿还债务金额
    def dev_cash_debtor_first_step(self):
        sql_data = DevDebtData().completed_debtor()

        total = len(sql_data)
        temp_list = []
        for i in range(total):
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            # print('债务减免金额:', sql_data[i][2])
            data = sql_data[i][0] + sql_data[i][1] - sql_data[i][2]
            temp_list.append(data)
        return temp_list

    def dev_cash_debtor_second_step(self):
        cash_data = DataFractionation().dev_cash_debtor_first_step()
        sum = 0
        for i in cash_data:
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            sum = i + sum
        return sum

    def dev_cash_agent_first_step(self):
        sql_data = DevDebtData().completed_agent()
        total = len(sql_data)
        temp_list = []
        for i in range(total):
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            # print('债务减免金额:', sql_data[i][2])
            data = sql_data[i][0]
            temp_list.append(data)
        return temp_list

    def dev_cash_agent_second_step(self):
        cash_data = DataFractionation().dev_cash_agent_first_step()
        sum = 0
        for i in cash_data:
            # print('本金为:', sql_data[i][0])
            # print('利息为:', sql_data[i][1])
            sum = i + sum
        return sum

if __name__ == '__main__':
    # # DataFractionation().dav_to_be_completed()
    # res = DataFractionation().dav_completed()
    # print('待完成解债金额:', res[0][2])
    # total = len(res)
    # print('total:', total)
    DataFractionation().dev_all_to_be_completed()