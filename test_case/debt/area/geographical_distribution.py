#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : geographical_distribution.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AreaDetail:
    """
    地区分布
    """

    def area(self):
        url = '/debt/staff/debt/geographical-distribution'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2020-11-27",
            "type": 5
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布查询失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print('地区分布查询结果为:', AreaDetail().area())
