#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : line_plan.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class LinePlan:
    """
    数据概览线型图
    """

    def query_line(self):
        url = '/debt/staff/debt/line-plan'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2020-11-27",
            "type": 10
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('数据概览线型图查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)数据概览线型图查询失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print('数据概览线型图查询结果为:', LinePlan().query_line())