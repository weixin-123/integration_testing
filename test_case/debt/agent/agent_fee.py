#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : agent_fee.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AgentFee:
    """
    经纪人费用缴纳记录
    """

    def agent_fee_pay(self):
        url = '/debt/staff/agent/fee'
        params = {
            "action": "query",
            "fields": [
                "agent_order_sn",
                "member_realname",
                "member_mobile",
                "agent_code",
                "agent_apply_cost",
                "pay_type",
                "pay_time"
            ],
            "page": 1,
            "params": [
                [
                    "member_mobile",
                    "like",
                    "187"
                ],
                [
                    "agent_code",
                    "like",
                    "WR"
                ],
                [
                    "created_at",
                    "in",
                    [
                        "2020-07-09",
                        "2020-12-30"
                    ]
                ]
            ],
            "size": 10
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('经纪人缴纳费用查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)查询失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print("经纪人缴纳费用为：", AgentFee().agent_fee_pay())
