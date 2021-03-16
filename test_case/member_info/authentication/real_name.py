#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/02/01
@File    : real_name.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest

f = Faker('zh_CN')
logging = LogingColor()
from test_case.member_info.login.login_app import LoginApp
read_user = ReadUserConfig()
class RealName:

    def real_name(self, phone, id_number, realname):
        """
        登录销巴APP  更改环境时，修改Post请求里面所需登录的环境
        :param phone:
        :return:
        """
        LoginApp().login_app(phone)
        login_url = "/member/member/member/auth"
        params = {
            "id_number": id_number,
            "auth_type": 2,
            "positive_card_image": 'http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-front-20210201102843698185.png',
            "back_card_image": 'http%3A%2F%2Fuser-qiniu.shall-buy.com%2Fuser-id-card-back-20210201102855444109.png',
            "realname": realname
        }
        result = HttpRequest.post(login_url, params, "app")
        if result["message"] == "success":
            logging.info('实名认证成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)实名认证失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    res = LoginApp().login_app(13436182072)