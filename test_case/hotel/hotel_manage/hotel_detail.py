#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/01/12
@File    : hotel_detail.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()

class HotelDetail:
    """
    后台获取城市
    """

    def city_children(self, id):
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