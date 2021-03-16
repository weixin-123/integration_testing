#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/18
@File    : recharge.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from test_case.car_v2.login_step.login_app import LoginApp
from test_case.car_v2.login_step.use_sql import UseSql

logging = LogingColor()

phone = LoginApp().login_app(15900606723)

class MemberRecharge:
    """
    充值账户
    """
    def member_recharge(self):
        data = UseSql().use_sql_select_seven(phone)
        url = "/finance/staff/account/add"
        params = {
            'accountId': data[1],
            'memberId': data[0],
            'balance': "30000"
        }
        result = HttpRequest.post(url, params,'admin')
        if result["message"] == "操作成功!":
            logging.info('账户充值成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)账户充值失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    print(MemberRecharge().member_recharge())