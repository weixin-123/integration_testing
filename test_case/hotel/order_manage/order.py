#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/01/12
@File    : order.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from faker import Faker
from test_case.hotel.order_manage.dev_use_sql import DevDebtData
import datetime

from test_case.hotel.order_manage.get_time import GetTime

logging = LogingColor()
f = Faker('zh_CN')
now_time = datetime.datetime.now()

class HotelDetail:
    """
    确认订单
    """

    def confirm(self, end_time, hotel_id, order_id):
        end_time = GetTime().change_day_time_format(end_time)
        room_id = DevDebtData().query_hotel_detail(hotel_id, order_id)[0][0]
        room_name = DevDebtData().query_hotel_detail(hotel_id, order_id)[0][1]
        bedName = DevDebtData().query_hotel_detail(hotel_id, order_id)[0][2]
        url = '/order/member/order/confirm'
        params = {
            "hotel_id": hotel_id,
            "room_id": room_id,
            "start_time": now_time.strftime("%Y-%m-%d"),
            # "end_time": f.future_date(),
            "end_time": end_time,
            "people_num": 1,
            "room_num": 1,
            "late_arrival_time": now_time.strftime("%Y-%m-%d %H:%M:%S"),
            "is_deduct_coin": 1,
            "customer_person": [
                {
                    "Name": "阿奴"
                }
            ],
            "mobile": "13436183072",
            "short_name": "CTrip",
            "room_name": room_name,
            "bedName": bedName,
            "remark": "有暖气",
            "order": {
                "type": "hotelv2"
            }
        }
        result = HttpRequest.post(url, params, 'app')
        if result["message"] == "success":
            logging.info('确认订单成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)确认订单失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    res = HotelDetail().confirm(1, 776692, 2)
    print(res)