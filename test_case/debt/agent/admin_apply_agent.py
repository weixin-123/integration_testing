#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/18
@File    : admin_apply_agent.py
"""
import time

from common.log_color import LogingColor
from common.request import HttpRequest
from Common_Functions.login_step.login_app import LoginApp

logging = LogingColor()


class ApplyAgent:
    """
    后台添加经纪人
    """

    def admin_agent_add(self, phone):
        LoginApp().login_app(phone)
        url = '/debt/staff/agent/create'
        params = {
            "member_mobile": phone,
            "agent_contract_url": "aa123456.com",
            "agent_apply_cost": 2000,
            "agent_contract_no": 123456,
            "agent_contract_name": "销巴解债经纪人",
            # "contract_sign_time": datetime.datetime.now()
            'contract_sign_time': time.strftime("%Y-%m-%d", time.localtime())
        }
        result = HttpRequest.post(url, params, 'admin')

        if result["message"] == "success":
            logging.info('后台申请经纪人成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)后台申请经纪人失败的原因：' + result['message'])
            return result["message"]

    """
    更新经纪人区域-二期
    """

    def admin_agent_update(self, agent_id):
        url = '/debt/staff/agent/update'
        params = {
            "agent_id": agent_id,
            "province": "上海",
            "city": "",
            "city_code": "510700"
        }
        print(params)
        result = HttpRequest.post(url, params, 'admin')

        if result["message"] == "success":
            logging.info('后台更新经纪人区域成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)后台更新经纪人区域失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    ApplyAgent().admin_agent_add('13436175942')
    # ApplyAgent().admin_agent_update(1)
