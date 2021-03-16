#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/03/10
@File    : login_store_app.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest

f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()
class LoginApp:

    def login_store_app(self, phone):
        """
        商户APP登录
        """
        login_url = "/store/index/store/member/login"
        params = {
            "client_id": "",
            "code": 123456,
            # 需要注册销巴会员调用register
            "is_app": 1,
            # "phone": 13436182070,
            "password": "aa123456",
            "username": phone
        }
        result = HttpRequest.post(login_url, params, "store_app")
        # result_json = result.json()
        if result["message"] == "success":
            logging.info('登录销巴商户APP成功(*^▽^*)')
            token = 'Bearer ' + result['data']['token']
            # 设置token
            read_user.set_login_info("store_app", "token", token)
        else:
            logging.error('(ಥ﹏ಥ)登录销巴生活商户后台失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    res = LoginApp().login_store_app(13436187694)