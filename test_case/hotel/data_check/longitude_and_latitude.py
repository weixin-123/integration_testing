#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/02/10
@File    : longitude_and_latitude.py
"""
from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest

f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()

# 校验数据
class Location:
    def get_list(self):
        """
        筛选的酒店列表
        传入经纬度
        """
        login_url = "/hotelv2/index/getList"
        params = {
                "city_code": "4",
                "sort": "complex",
                "area_latitude": "29.999285",
                "area_longitude": "108.114069",
                "page": 1,
                "longitude": "106.610036",
                "latitude": "29.648608"
        }
        result = HttpRequest.post(login_url, params, "app")
        if result["message"] == "success":
            logging.info('订单取消成功(*^▽^*)')
            return result["data"]["list"]
        else:
            logging.error('(ಥ﹏ಥ)订单取消失败的原因：' + result['message'])
            return result["message"]

if __name__ == "__main__":
    res = Location().get_list()