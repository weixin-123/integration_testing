#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : admin_agent_detail.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AdminDetail:
    """
    经纪人列表
    """

    def agent_query(self, member_realname, member_mobile, agent_code, freeze):
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
                    member_realname
                ],
                [
                    # 会员手机号
                    "member_mobile",
                    "like",
                    member_mobile
                ],
                [
                    # 经纪人代码
                    "agent_code",
                    "like",
                    agent_code
                ],
                [
                    # 冻结(0:否, 1:是，2:合同到期)
                    "freeze",
                    "=",
                    freeze
                ],
                [
                    # 创建时间
                    "created_at",
                    "in",
                    [
                        "2020-07-09",
                        "2021-12-30"
                    ]
                ],
                [
                    # 有效期
                    "term_validity",
                    "in",
                    [
                        "2020-07-09",
                        "2022-12-30"
                    ]
                ]
            ],
            # 页数
            "size": 10
        }
        result = HttpRequest.post_json(url, data, 'admin')
        if result["message"] == "success":
            logging.info('经纪人列表查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)经纪人列表查询失败的原因：' + result['message'])
            return result["message"]

    """
    获取经纪人导出
    """

    def agent_export(self, member_realname, member_mobile, agent_code, freeze, agent_start_time, agent_end_time,
                     created_at):
        url = '/debt/staff/agent/list'
        data = {
            "action": "export",
            "fields": {
                "member_realname": member_realname,
                "member_mobile": member_mobile,
                "agent_code": agent_code,
                "freeze": freeze,
                "agent_apply_cost": 2000,
                "agent_start_time": agent_start_time,
                "agent_end_time": agent_end_time,
                "created_at": created_at
            }
        }
        result = HttpRequest.post_json(url, data, 'admin')
        if result["message"] == "success":
            logging.info('获取经纪人导出成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)获取经纪人导出失败的原因：' + result['message'])
            return result["message"]

    """
    经纪人详情-二期
    """

    def agent_detail(self, agent_id):
        url = '/debt/staff/agent/detail'
        data = {
            "agent_id": agent_id
        }
        result = HttpRequest.post_json(url, data, 'admin')
        if result["message"] == "success":
            logging.info('经纪人详情查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)经纪人详情查询失败的原因：' + result['message'])
            return result["message"]

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
    # # 会员真实姓名 会员手机号 经纪人代码 冻结状态 创建时间
    # AdminDetail().agent_query('豆豆', '13436167502', 'WR0001', '0')
    # 经纪人姓名 经纪人手机号 经纪人代码 冻结状态 费用 经纪人有效期开始时间 经纪人有效期结束时间 创建时间
    # AdminDetail().agent_export('豆豆', '13436167502', 'WR0001', '0', '2020-10-14 11:13:41', '2021-12-31 11:13:41', '2020-10-08 10:32:18')
    # 经纪人详情
    AdminDetail().agent_detail(1)
    # # 经纪人费用缴纳记录
    # AdminDetail().agent_fee_pay()
