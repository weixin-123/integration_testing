#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/08
@File    : order_status.py
"""
from test_case.debt.data_overview.data_fractionation import DataFractionation
from test_case.debt.data_overview.dev_use_sql import DevDebtData


class OrderCheck:
    def test_assert_data(self):
        # 10：待债权人确认
        creating_one = DevDebtData().query_dev_count(10)
        # 20:待提交审核
        creating_two = DevDebtData().query_dev_count(20)
        # 25：待平台审核
        creating_three = DevDebtData().query_dev_count(25)
        # 30：待财务审核
        creating_four = DevDebtData().query_dev_count(30)
        # 40：待合同审批
        creating_five = DevDebtData().query_dev_count(40)
        # 50：待合同签名
        creating_six = DevDebtData().query_dev_count(50)
        # 待完成解债笔数
        creating_total = creating_one + creating_two + creating_three + creating_four + creating_five + creating_six
        print('待完成解债笔数:', creating_total)

        # 70：债权人驳回
        completed_one = DevDebtData().query_dev_count(70)
        # 80：平台驳回
        completed_two = DevDebtData().query_dev_count(80)
        # 85：财务驳回
        completed_three = DevDebtData().query_dev_count(85)
        # 90：合同审批驳回
        completed_four = DevDebtData().query_dev_count(90)
        # 100：合同撤回
        completed_five = DevDebtData().query_dev_count(100)
        # 110：合同作废
        completed_six = DevDebtData().query_dev_count(110)
        # 120：债务人撤回,（废弃）
        # completed_seven = DevDebtData().query_dev_count(120)
        # 60：还款中（签名已完成）
        creating_seven = DevDebtData().query_dev_count(60)

        # 130: 订单完成
        completed_eight = DevDebtData().query_dev_count(130)
        # 已完成解债笔数
        creating_total = completed_one + completed_two + completed_three + completed_four + completed_five + completed_six + creating_seven + completed_eight
        print('已完成解债笔数:', creating_total)

        # repayment_quota 每月还款额度 repayment_money 已还款微币 repayment_period 已还款期数

        # # 待完成解债金额 非 60 130
        # completting_total = DataFractionation().dev_cash_completing_second_step()
        # print("待完成解债金额:", completting_total)
        #
        # # 已完成解债金额  60 130
        # completed_total = DataFractionation().dev_cash_completed_second_step()
        # print("已完成解债金额:", completed_total)
        #
        # # 解债客单价  已完成的解债金额/已完成的解债数
        # total = DevDebtData().completed_debt_cash_total()[0][0]
        # print("解债客单价:", completed_total / total)
        #
        # # 已收需偿还债务金额 平台收到的债务人需偿还债务金额（即债务人的打款金额）
        # total = DataFractionation().dev_cash_debtor_second_step()
        # print("已收需偿还债务金额:", total)
        #
        # # 某用户已还债权微币
        # res = DataFractionation().dav_completed()
        # total = len(res)
        # print('已还款总期数:', total)
        # repayment_quota = res[0][1]
        # repaymented = repayment_quota * total
        # print('已还债权微币:', repaymented)
        # # 某用户待还债权微币
        # repaymentting = DataFractionation().dav_completed()[0][2]
        # print('待还债权微币:', repaymentting)
        #
        # # 总待还债权微币
        # all_repaymentting = DataFractionation().dev_all_to_be_completing()
        # print('待还债权微币:', all_repaymentting)
        # #
        # # 总已还债权微币
        # all_repaymented_first= DataFractionation().dev_all_to_be_completed_first()
        # all_repaymented_second= DataFractionation().dev_all_to_be_completed_second()
        # all_repaymented = all_repaymented_first + all_repaymented_second
        # print('已还债权微币:', all_repaymented)
        # #
        # # 已结算经纪人劳务费 agent_profit status 60/130
        # total = DataFractionation().dev_cash_agent_second_step()
        # print('已结算经纪人劳务费:', total)
        #
        # # 已结算经纪人团队管理津贴



if __name__ == '__main__':
    OrderCheck().test_assert_data()
