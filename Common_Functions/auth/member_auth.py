#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/03/10
@File    : member_auth.py
"""
import json

from common.request import HttpRequest
from common.log_color import LogingColor

logging = LogingColor()

from Common_Functions.register.store_app.random_data import Random_Data
from Common_Functions.login_step.login_app import LoginApp
from Common_Functions.register.store_app.use_sql import UseSql


class Register_Member:

    def auth(self, id_number, phone):
        LoginApp().login_app(phone)
        register_url = "/member/member/member/auth"
        params = {
            "id_number": id_number,
            "auth_type": 2,
            "back_card_image": "http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-back-20210312104743268150.png",
            "positive_card_image": "http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-front-20210312104739258183.png",
            "realname": phone
        }
        # logging.info("请求参数:" + str(params))
        temp_params = json.dumps(params)
        result = HttpRequest.post(register_url, temp_params, service_name="app")
        # result_json = result.json()
        # print(result_json)
        if result["message"] == "success":
            logging.error('实名认证成功')
        else:
            logging.error('账户已存在')

    def agree(self, member_id):
        register_url = "/member/staff/member/auth/agree"
        params = {
            "id_number": member_id
        }
        # logging.info("请求参数:" + str(params))
        temp_params = json.dumps(params)
        result = HttpRequest.post(register_url, temp_params, service_name="admin")
        # result_json = result.json()
        # print(result_json)
        if result["message"] == "success":
            logging.error('实名认证成功')
        else:
            logging.error('账户已存在')



if __name__ == "__main__":
    # for i in range(5):
    res = Register_Member().auth('110101199503072910', 13436132917)
    # Register_Member().agree(6930232)