#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : agent_list.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()
class AgentList:
    """
    获取经纪人列表
    """
    def agent_list(self):
        url = '/debt/staff/agent/list'
        data = {
            "action": "query",
            "fields": [
                "member_realname",
                "member_mobile",
                "agent_code",
                "agent_apply_cost",
                "freeze",
                "created_at",
                "agent_start_time",
                "agent_end_time"
            ],
            "page": 1,
            "params": [
                [
                    # 会员真实姓名
                    "member_realname",
                    "like",
                    "小熊"
                ],
                [
                    # 会员手机号
                    "member_mobile",
                    "like",
                    "15900606723"
                ],
                [
                    # 经纪人代码
                    "agent_code",
                    "like",
                    "WR"
                ],
                [
                    # 冻结(0:否, 1:是，2:合同到期)
                    "freeze",
                    "=",
                    "0"
                ],
                [
                    # 创建时间
                    "created_at",
                    "in",
                    [
                        "2020-07-09",
                        "2020-12-30"
                    ]
                ],
                [
                    # ？？？
                    "term_validity",
                    "in",
                    [
                        "2020-09-24",
                        "2021-9-23"
                    ]
                ]
            ],
            # 页数？
            "size": 10
        }
        result = HttpRequest.post(url, data, 'admin')
        print(result)
        if result["message"] == "success":
            logging.info('申请经纪人成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)申请经纪人失败的原因：' + result['message'])
            return result["message"]