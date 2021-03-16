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

from Common_Functions.register.store_app.use_sql import UseSql


class Register_Member:

    def create_check(self, phone):
        register_url = "/store/index/store/create_check"
        params = {
            "code": 123456,
            "phone": phone
        }
        # logging.info("请求参数:" + str(params))
        temp_params = json.dumps(params)
        result = HttpRequest.post(register_url, temp_params, service_name="store_app")
        # result_json = result.json()
        # print(result_json)
        if result["message"] == "success":
            return result['data']['id']
        else:
            logging.error('%s(ಥ﹏ಥ)账户已存在')

    def register_store_app_member(self, phone, username):
        """
        注册销巴线下App
        """
        member_id = Register_Member().create_check(phone)
        register_url = "/store/index/store/create"
        params = {
            "member_id": member_id,
            "password_confirmation": "aa123456",
            "password": "aa123456",
            "code":123456,
            "username": username
        }
        # logging.info("请求参数:" + str(params))
        temp_params = json.dumps(params)
        result = HttpRequest.post(register_url, temp_params, service_name="store_app")
        # result_json = result.json()
        print(result)
        if result["message"] == "success":
            logging.info('%s注册销巴商户成功(*^▽^*)' % phone)
            return phone
        else:
            logging.error('%s(ಥ﹏ಥ)注册销巴商户失败的原因：' % phone)
            return result["message"]


if __name__ == "__main__":
    # for i in range(5):
    res = Register_Member().register_store_app_member(13436114962, "伊琨")