#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : publish_order.py
"""
<<<<<<< HEAD
import time
=======
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class PublishOrder:
    """
    债务人发布订单
    """

<<<<<<< HEAD
    def qianti_pubulish(self, id):
        url = '/debt/member/cert/is-cert'
        params = {
            "member_id": id
        }
        result = HttpRequest.post(url, params, 'app')
        print(result)
        if result["message"] == "success":
            logging.info('接口调用成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)接口调用失败的原因：' + result['message'])

    def publish(self):
        # LoginApp().login_app(phone)
        # 债务人 debtor
        # 债权人 creditor
        url = '/debt/member/debtor/publish-order_manage'
        params = {
            "phone": "13436182070",
            "name": "阿新",
            "agent_code": "WR0001",
            "amount": 10000,
            "interest_amount": 0,
            "images": [
                "voucher/20200930024644831.png",
                "voucher/20200930024651712.png"
            ]
=======
    def publish(self):
        url = '/debt/member/debtor/publish-order'
        params = {
            "creditor_phone": "15900606723",
            "creditor_name": "小熊",
            "agent_code": "WR00016",
            "amount": 1000,
            "interest_amount": 1,
            "pay_account": "66666666",
            "payment_info": ["voucher/20201210110529278.jpeg"]
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('债务人发起订单成功(*^▽^*)')
            return result['data']['id']

        else:
            logging.error('(ಥ﹏ಥ)债务人发起订单失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
<<<<<<< HEAD
    # 前提
    # PublishOrder().qianti_pubulish(2115202)
    for i in range(5):
        time.sleep(5)
        print("订单id为：", PublishOrder().publish())
=======
    print("订单id为：", PublishOrder().publish())
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
    # ApplyAgent().agent_list()
