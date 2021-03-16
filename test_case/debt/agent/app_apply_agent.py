#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/07
@File    : app_apply_agent.py
"""

from common.log_color import LogingColor
from common.request import HttpRequest
from Common_Functions.login_step.login_app import LoginApp
from test_case.debt.agent.dev_use_sql import DevDebtData

logging = LogingColor()




class AppApplyAgent:
    """
    实名认证
    """

    def auth(self, phone, realname, id_number):
        LoginApp().login_app(phone)
        url = '/member/member/member/auth'
        params = {
            # 身份证号
            "id_number": id_number,
            "auth_type": 2,
            'back_card_image': 'http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-back-20201219141039195158.png',
            'positive_card_image': 'http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-back-20201219141039195158.png',
            'realname': realname
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('实名认证成功快去后台通过吧(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)实名认证失败的原因：' + result['message'])

    """
    更新成为粉丝-二期
    """

    def update(self, my_phone, agent_phone, agent_id):
        LoginApp().login_app(my_phone)
        url = '/debt/member/agent/agent-update'
        params = {
            "member_mobile": agent_phone,
            "agent_id":agent_id

        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('成为粉丝成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)成为粉丝失败的原因：' + result['message'])

    """
    确认订单
    """

    def order_confirm(self, phone):
        member_id = DevDebtData().query_id(phone)[0][0]
        url = '/order_manage/member/order_manage/confirm'
        params = {
            "order_manage": {
                "type": "debt",
                "member_id": member_id,
                "client": 10

            },
            "order_amount": 2000,
            "is_use_deduct_credit2": 1
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('确认订单操作成功(*^▽^*)')
            return result['data']['order_manage']['confirm']
        else:
            logging.error('(ಥ﹏ಥ)确认订单操作失败的原因：' + result['message'])
            return result["message"]

    """
    创建订单
    """

    def app_agent_add(self, confirm):
        url = '/order_manage/member/order_manage/create'
        params = {
            "order_manage": {
                "type": "debt",
                "client": 10,
                "confirm": confirm
            },
            "is_use_deduct_credit2": 1,
            "order_amount": 2000,
            "agent_introduce": '我的销巴经纪人'
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('创建订单操作成功(*^▽^*)')
            return result['data']['ordersn']
        else:
            logging.error('(ಥ﹏ಥ)创建订单操作失败的原因：' + result['message'])
            return result["message"]

    """
    支付
    """

    def pay(self, ordersn):
        url = '/order_manage/member/order_manage/pay'
        params = {
            "ordersn": ordersn,
            "money": 2000,
            "pay_type": 4,
            "password": "131013"
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('支付订单操作成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)支付订单操作失败的原因：' + result['message'])
            return result["message"]

    """
    合同审批
    """

    def change_status(self):
        for i in range(2):
            contract_id = contract[0][i]
            url = '/contract/staff/contract/change/status'
            params = {
                "contract_id": contract_id,
                "contract_status": 1
            }
            result = HttpRequest.post(url, params, 'admin')
            if result["message"] == "success":
                logging.info('合同审批成功(*^▽^*)')
            else:
                logging.error('(ಥ﹏ಥ)合同审批失败的原因：' + result['message'])
                return result["message"]

    """
    签订解债经纪人合作协议
    """

    def agent_sign(self):
        contract_id = contract[0][0]
        url = '/debt/member/agent/sign'
        params = {
            "contract_id": contract_id,
            "seal": "sign_lufei.png",
            "url": "http://www.baidu.com"
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('解债经纪人合作协议签订成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)解债经纪人合作协议签订失败的原因：' + result['message'])
            return result["message"]

    """
    签署经纪人商标使用许可合同
    """

    def logo_sign(self):
        contract_id = contract[0][1]
        url = '/debt/member/agent/logo-sign'
        params = {
            "contract_id": contract_id,
            "seal": "sign_lufei.png",
            "url": "http://www.baidu.com"
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('经纪人商标使用许可合同签订成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)经纪人商标使用许可合同失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # # 实名认证
    # AppApplyAgent().auth(13436167502, '豆豆', 333333)
    # PublishOrder().qianti_pubulish(2115188)
    #
    # # # 成为粉丝 自己的号码  经纪人号码 经纪人id
    # AppApplyAgent().update(13436183072, 13436182070, 1)
    #
    # # # # 确认订单
    # confirm = AppApplyAgent().order_confirm(13436183072)
    # # 创建订单
    # ordersn = AppApplyAgent().app_agent_add(confirm)
    # # # 支付
    # AppApplyAgent().pay(ordersn)

    # # 前提
    # # PublishOrder().qianti_pubulish(2115203)
    # # # # #
    contract = DevDebtData().query_contract(3)
    # # 合同审批
    AppApplyAgent().change_status()
    # 签订解债经纪人合作协议
    AppApplyAgent().agent_sign()
    #  签署经纪人商标使用许可合同
    AppApplyAgent().logo_sign()
