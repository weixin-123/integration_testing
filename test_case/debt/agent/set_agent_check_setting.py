#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/14
@File    : set_agent_check_setting.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class SetAgentCheckSetting:
    """
    财务审核通过
    """

    def info(self):
        url = '/debt/staff/setting/get-agent-admin_operation-setting-info'
        result = HttpRequest.post_json(url, None, 'admin')
        if result["message"] == "success":
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ) 财务审核失败的原因：' + result['message'])
            return result["message"]

    def edit(self):
        url = '/debt/staff/setting/set-agent-admin_operation-setting'
        params = {
            "agent_check_status": 1,
            "director_number_index": 11,
            "director_achievement_index": 3000000,
            "director_allowance_rate": 0.3,
            "manager_number_index": 21,
            "manager_achievement_index": 10000000,
            "manager_allowance_rate": 0.5,
            "director_keep_number_index": 0,
            "director_keep_achievement_index": 0,
            "manager_keep_promotion_index": 0,
            "manager_keep_achievement_index": 0
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ) 财务审核失败的原因：' + result['message'])
            return result["message"]

    def list(self):
        url = '/debt/staff/supplement-order_manage/list'
        params = {
            "action": "query"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ) 财务审核失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    SetAgentCheckSetting().list()
