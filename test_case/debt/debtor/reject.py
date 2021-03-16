#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : reject.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from test_case.debt.debtor.publish_order import PublishOrder

logging = LogingColor()


class RejectDebtor:
    """
    债权人驳回
    """

    def reject_debtor(self, id):
<<<<<<< HEAD
        url = '/debt/member/creditor/creditor-order_manage/reject'
        params = {
            "order_id": id,
            "creditor_reject_remark": "凭证模糊不清"
=======
        url = '/debt/member/creditor/creditor-order/reject'
        params = {
            "order_id": id,
            "creditor_reject_remark": "看你不舒服"
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('债权人驳回成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)债权人驳回失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # order_id = PublishOrder().publish()
<<<<<<< HEAD
    RejectDebtor().reject_debtor(2)
=======
    RejectDebtor().reject_debtor(47)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
