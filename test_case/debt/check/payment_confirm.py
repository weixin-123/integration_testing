#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : payment_confirm.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class PaymentConfirm:
    """
    财务审核通过
    """

    def examine(self, id):
        url = '/debt/staff/finance/payment/confirm'
        params = {
            "id": id
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info(' 财务审核通过(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 财务审核失败的原因：' + result['message'])
            return result["message"]

    """
    财务审核不通过
    """
    def reject(self, id):
        url = '/debt/staff/finance/payment/reject'
        params = {
            "id": id,
            "remark": "没有收到打款，通过打款凭证查看您打错款了"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('财务审核不通过请求成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)财务审核不通过请求失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    # order_id = PublishOrder().publish()
    # 财务审核通过
    PaymentConfirm().examine(49)

    # # 财务审核不通过
    # PaymentConfirm().reject(49)