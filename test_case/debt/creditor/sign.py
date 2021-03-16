#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : sign.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from Common_Functions.login_step.login_app import LoginApp

logging = LogingColor()


class Sign:
    """
    债权人签署合同
    """

    def debtor(self, id):
        LoginApp().login_app(13436182072)
        url = '/debt/member/creditor/creditor-order_manage/sign-role'
        params = {
            "order_id": str(id),
            "seal": "seal/20201210142811165.png",
            "mobile": "13436182072",
            "code": "123456"
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info(' 债权人签署合同成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 债权人签署合同失败的原因：' + result['message'])
            return result["message"]

    """
    债务人签署合同
    """

    def creditor(self, id):
        LoginApp().login_app(13436137948)
        url = '/debt/member/debtor-order_manage/sign-contract'
        params = {
            "order_id": str(id),
            "seal": "sign_lufei.png",
            "code": "123456",
            "mobile": "13436137948"
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('债务人签署合同成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)债务人签署合同失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # order_id = PublishOrder().publish()
    # 债务人签署合同
    Sign().debtor(21)
    # 债权人签署合同
    # Sign().creditor(21)

# 查询签章
# SELECT * FROM `life_contract_list_role` where contract_id = 138
