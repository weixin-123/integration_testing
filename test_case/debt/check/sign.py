#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : sign.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class Sign:
    """
    债权人签署合同
    """

    def debtor(self, id):
        url = '/debt/member/creditor/creditor-order/sign-role'
        params = {
            "order_id": str(id),
            "seal": "seal/20201210142811165.png",
            "mobile": "15900606723",
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
        url = '/debt/member/debtor-order/sign-contract'
        params = {
            "order_id": str(id),
            "seal": "sign_lufei.png",
            "code": "123456",
            "mobile": "13436182072"
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
    # Sign().debtor(49)
    # 债权人签署合同
    Sign().creditor(49)

# 查询签章
# SELECT * FROM `life_contract_list_role` where contract_id = 138
