#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : platform_status.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class ExamineAdopt:
    """
    平台审核通过
    """

    def examine(self, id):
        url = '/debt/staff/order_manage-apply/examine/adopt'
        params = {
            "id": id
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('平台审核通过(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)债平台审核失败的原因：' + result['message'])
            return result["message"]

    """
    平台审核不通过
    """
    def reject(self, id):
        url = '/debt/staff/order_manage-apply/examine/reject'
        params = {
            "id": id,
            "reject_remark": "没有理由"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('平台审核驳回成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)平台审核驳回失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    # order_id = PublishOrder().publish()
    # 平台审核通过
    ExamineAdopt().examine(49)
    # # 平台审核驳回
    # ExamineAdopt().reject(49)