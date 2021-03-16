#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : agent_detail.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AgentDetail:
    """
    经纪人数据
    """

    def detail(self):
        url = '/debt/staff/debt/agent-data'
        params = {
            "sort_criteria": 4,
            "identity": 0,
            "city": 441800,
            "mobile": 18023332333,
            "agent_code": "WR0004"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    print('查询的经纪人信息为:', AgentDetail().detail())
