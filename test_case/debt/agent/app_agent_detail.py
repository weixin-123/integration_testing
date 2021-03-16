#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : app_agent_detail.py
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

    """
    业绩明细-二期
    """

    def performance_detail(self, phone):
        url = '/debt/member/agent/performance-detail'
        params = {
            "time": "2020-11",
            # 0：加入团队时间由高到底1：加入团队时间由高到底
            "join_time": 0,
            # 0：业绩由高到低 1：业绩由低到高）
            "achievement": 0,
            "condition": phone
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]

    """
    津贴明细-二期
    """

    def allowance_detail(self):
        url = '/debt/member/agent/allowance'
        params = {
            "time": "2020-11"
        }
        result = HttpRequest.post_json(url, params, 'app')
        if result["message"] == "success":
            logging.info('津贴明细查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)津贴明细查询失败的原因：' + result['message'])
            return result["message"]

    """
   经纪人考核
    """

    def agent_task(self):
        url = '/debt/inner/agent/auto-task'
        result = HttpRequest.post_json(url, None, 'inner')
        if result["message"] == "success":
            logging.info('业绩已结算，请自行查看晋级/保级的情况哦(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)接口请求失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # print('查询的经纪人信息为:', AgentDetail().detail())
    # AgentDetail().performance_detail(13436183072)
    # AgentDetail().allowance_detail()
    AgentDetail().agent_task()

#晋升  总业绩-指标 *百分比
#保级 总业绩*百分比