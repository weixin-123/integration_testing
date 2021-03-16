#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/07
@File    : apply_agent.py
"""
import datetime

from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class ApplyAgent:
    """
    添加经纪人
    """

    def agent_add(self, phone):
        url = '/debt/staff/agent/create'
        params = {
            "member_mobile": phone,
            "agent_contract_url": "132132aba",
            "agent_apply_cost": 2000,
            "agent_contract_no": 12131,
            "agent_contract_name": "销巴解债经纪人",
            "contract_sign_time": datetime.datetime.now()
        }
        result = HttpRequest.post(url, params, 'admin')

        if result["message"] == "success":
            logging.info('申请经纪人成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)申请经纪人失败的原因：' + result['message'])
            return result["message"]




if __name__ == '__main__':
    ApplyAgent().agent_add('13436182072')
    # ApplyAgent().agent_list()
