#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/11
@File    : login_app.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest

f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()
class LoginApp:

    def login_app(self, phone):
        """
        登录销巴APP  更改环境时，修改Post请求里面所需登录的环境
        :param phone:
        :return:
        """
        login_url = "/member/index/member/phone/login"
        params = {
            "code": 123456,
            "device_id": "6c33422d1b85e16d",
            # 需要注册销巴会员调用register
            "phone": phone,

            # "phone": 13436182070,
            "android_version": "2.2.4",
            "client_id": "98063512033aefb04328ea6bb8afdc42"
        }
        logging.info("请求URL：" + login_url)
        logging.info("请求参数:" + str(params))
        result = HttpRequest.post(login_url, params, "app")
        print(result)
        # result_json = result.json()
        if result["message"] == "success":
            logging.info('登录销巴APP成功(*^▽^*)')
            token = 'Bearer ' + result['data']['token']
            # 设置token
            read_user.set_login_info("app", "token", token)
            return phone
        else:
            logging.error('(ಥ﹏ಥ)注登录销巴APP失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    res = LoginApp().login_app(13436182072)
