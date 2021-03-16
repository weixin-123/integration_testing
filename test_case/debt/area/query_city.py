#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : query_city.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class QueryArea:
    """
    地区分布
    """

    def query_area(self):
        url = '/debt/staff/debt/query-city'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2020-11-29",
            "city": 45
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]

    def query_province(self):
        url = '/debt/staff/debt/distribution'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2020-11-29"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print('地区分布市查询结果为:', QueryArea().query_area())
    print('地区分布省查询结果为:', QueryArea().query_province())