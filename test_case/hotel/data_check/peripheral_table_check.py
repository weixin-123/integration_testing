#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/02/10
@File    : peripheral_table_check.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
import requests

f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()
class PeripheralCheck:
    def peripheral(self):
        """
        省市数据校验
        """
        login_url = "https://developer.amap.com/service/api/restapi"
        params = {
            'address':'渝中区',
            'city':''
        }
        result = requests.get(login_url, params)
        print(result)
        if result["info"] == "OK":
            logging.info('订单取消成功(*^▽^*)')
            return result["data"]["list"]
        else:
            logging.error('(ಥ﹏ಥ)订单取消失败的原因：' + result['message'])
            return result["message"]

if __name__ == "__main__":
    res = PeripheralCheck().peripheral()