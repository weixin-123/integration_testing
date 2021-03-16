#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : adopt.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AdoptDebtor:
    """
    债权人通过订单
    """

<<<<<<< HEAD
    def adopt(self, id):
        url = '/debt/member/creditor/creditor-order_manage/adopt'
        params = {
            "order_id": id
=======
    def adoptdebtor(self, id):
        url = '/debt/member/creditor/creditor-order/adopt'
        params = {
            "order_id" : id
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('债权人确认订单成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)债权人确认订单失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # order_id = PublishOrder().publish()
    id = 38
<<<<<<< HEAD
    AdoptDebtor().adopt(id)
=======
    AdoptDebtor().adoptdebtor(id)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
