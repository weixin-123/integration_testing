#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/03/01
@File    : register_store.py
"""
import json

from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest
from Common_Functions.login_step.login_store_app import LoginApp

f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()


class RegisterMerchant:

    def register_store(self, username, shop_name, phone, cert_name):
        """
        注册商家
        :param phone:
        :return:
        """
        LoginApp().login_store_app(phone)
        login_url = "/offshop/store/canteen/join/apply"
        params = {
            "contact": username,
            "shop_name": shop_name,
            "tel": phone,
            "apply_quota": "150000.00",
            "logo": "http://shop-qiniu.shall-buy.com/shop-20210311103551377378.jpg",
            "lease_contract": ["contract/20210312091125174.jpg"],
            "cert_name": cert_name,
            "images": [
                [1860, "http://shop-qiniu.shall-buy.com/shop-20210311103654621689.jpg"]
            ]
        }
        temp_params=json.dumps(params)
        result = HttpRequest.post(login_url, temp_params, "store_app")
        if result["message"] == "success":
            logging.info('销巴商户注册成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)销巴商户注册失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    res = RegisterMerchant().register_store("阿猫", "阿猫喵喵宠物店", 13436142190, "阿猫的营业执照")
