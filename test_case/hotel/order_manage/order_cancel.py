#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/02/01
@File    : order_cancel.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest

f = Faker('zh_CN')
logging = LogingColor()
from test_case.member_info.login.login_app import LoginApp

read_user = ReadUserConfig()


class OrderCancel:

    def cancel(self, phone, order_sn):
        """
        酒店订单取消
        :param phone:
        :return:
        """
        LoginApp().login_app(phone)
        login_url = "/hotelv2/member/order/cancel"
        params = {
            "order_sn": str(order_sn),
            "cancel_reason": "测试"
        }
        result = HttpRequest.post(login_url, params, "app")
        if result["message"] == "success":
            logging.info('订单取消成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)订单取消失败的原因：' + result['message'])
            return result["message"]

if __name__ == "__main__":
    res = OrderCancel().cancel(13436182072, 412102030945551951)
# 412102051143027585 412102051040467650 412102051040027049 412102051039169250 412102050955476810 412102050953555111 412102050950515525