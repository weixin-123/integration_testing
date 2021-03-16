#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/18
@File    : recharge.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from Common_Functions.login_step import UseSql

logging = LogingColor()



class MemberRecharge:
    """
    充值账户  更改环境时，需要修改post请求和nase_config.ini里面所要增值的环境
    """
    def member_recharge(self, phone):
        data = UseSql().use_sql_select_seven(phone)
        url = "/finance/staff/account/add"
        params = {
            'accountId': data[1],
            'memberId': data[0],
            'balance': "300000",
            'content': '测试'
        }
        result = HttpRequest.post_json(url, params,'admin')
        if result["message"] == "操作成功!":
            logging.info('账户充值成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)账户充值失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    print(MemberRecharge().member_recharge(13436182072))