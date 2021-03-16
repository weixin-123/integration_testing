#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : debt_test.py
"""
<<<<<<< HEAD
from test_case.debt.admin_operation.platform_status import ExamineAdopt
=======
from test_case.debt.check.examine_adopt import ExamineAdopt
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
from test_case.debt.creditor.adopt import AdoptDebtor
from test_case.debt.creditor.up_iou import CreditorUpIou
from test_case.debt.debtor.publish_order import PublishOrder
from test_case.debt.debtor.reject import RejectDebtor
<<<<<<< HEAD
from test_case.debt.admin_operation.finance_status import PaymentConfirm
from test_case.debt.admin_operation.contract_status import Contract
from test_case.debt.creditor.sign import Sign
from test_case.debt.admin_operation.dev_use_sql import DevDebtData
=======
from test_case.debt.check.payment_confirm import PaymentConfirm
from test_case.debt.check.contract import Contract
from test_case.debt.check.sign import Sign
from test_case.debt.check.test_use_sql import DevDebtData
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587


# '订单状态 10：待债权人确认，20:待提交审核 25：待平台审核 30：待财务审核，40：待合同审批，50：待合同签名，60：还款中（签名已完成），
# 70：债权人驳回，80：平台驳回，85：财务驳回，90：合同审批驳回，100：合同撤回，110：合同作废，120：债务人撤回,（废弃） 130:订单完成',

<<<<<<< HEAD
#   40
=======
#   110 130
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
from test_case.debt.update_time.order_end import OrderTime


class DebtProcess:
    def process(self,id):
<<<<<<< HEAD
        # # #  债务人发布订单
        # # print("订单id为：", PublishOrder().publish())
        # #
        # # # # # 债权人驳回 传入订单号
        # # RejectDebtor().reject_debtor(id)
        # # # # # # # # 债权人通过 传入订单号
        AdoptDebtor().adopt(id)
        # # # # # # # # # # #
        # # # # # # # # # # # 债权人上传借条
        CreditorUpIou().up_iou(id)
        # # # # # # # # # # #
        # # # # # # # # # # # 平台审核通过
        ExamineAdopt().examine(id)
        # # # # # # # # # # # # # # 平台审核驳回
        # ExamineAdopt().reject(id)
        # # # # # # # #
        # # # # # # # # # # # # 财务审核通过
        PaymentConfirm().examine(id)
        # # # # # # # # # # # # # 财务审核不通过
        # PaymentConfirm().reject(id)
        # # # # # # # # # # # # #
        # # # # # # # # # # # # # # # 合同审批通过
        contract_id = DevDebtData().query_contract(id)[0][0]
        Contract().contract_pass(contract_id)
        # # # # # # 合同审核驳回
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().reject(contract_id)
        # # # 合同审核撤销
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().withdraw(contract_id)
        # # # 合同审核失效
        # # # Contract().efficacy(id)
        # # # # 债务人签署合同
        # Sign().debtor(id)
        # # # # # # # # 债权人签署合同
        # Sign().creditor(id)
        # # # # 合同作废
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().void(contract_id)
        # # # 定时任务
        # OrderTime().test_time()

if __name__ == '__main__':
    DebtProcess().process(16)
=======
        # #  债务人发布订单
        # print("订单id为：", PublishOrder().publish())
        #
        # # 债权人驳回 传入订单号
        # RejectDebtor().reject_debtor(id)
        # # # 债权人通过 传入订单号
        # AdoptDebtor().adoptdebtor(id)
        # #
        # # 债权人上传借条
        # CreditorUpIou().creditor_up_iou(id)
        #
        # # 平台审核通过
        # ExamineAdopt().examine(id)
        # # 平台审核驳回
        # ExamineAdopt().reject(id)
        # #
        # # 财务审核通过
        # PaymentConfirm().examine(id)
        # # # 财务审核不通过
        # PaymentConfirm().reject(id)
        # #
        # # # 合同审批通过
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().contract_pass(contract_id)
        # # 合同审核驳回
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().reject(contract_id)
        # 合同审核撤销
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().withdraw(contract_id)
        # 合同作废
        # contract_id = DevDebtData().query_contract(id)[0][0]
        # Contract().void(contract_id)

        # # 债务人签署合同
        Sign().debtor(id)
        # 债权人签署合同
        Sign().creditor(id)
        # 定时任务
        OrderTime().test_time()

if __name__ == '__main__':
    DebtProcess().process(54)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
