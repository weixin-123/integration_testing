#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : up_iou.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class CreditorUpIou:
    """
    债务人上传借条
    """

<<<<<<< HEAD
    def up_iou(self, id):
        url = '/debt/member/creditor/creditor-order_manage/up-iou'
        params = {
            "order_id": id,
            "receipt_img": ["test/debt/20201228163113852.jpeg"]
=======
    def creditor_up_iou(self, id):
        url = '/debt/member/creditor/creditor-order/up-iou'
        params = {
            "order_id": id,
            "receipt_img": ["1600681924759-review.png"]
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('债务人上传借条成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)债务人上传借条失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # order_id = PublishOrder().publish()
<<<<<<< HEAD
    CreditorUpIou().up_iou(49)
=======
    id = 49
    CreditorUpIou().creditor_up_iou(id)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
