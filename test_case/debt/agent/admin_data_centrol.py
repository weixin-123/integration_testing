#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/18
@File    : admin_data_centrol.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AdminDataCentrol:
    """
    数据中心 --- 经纪人数据-二期 筛选
    """

    def query(self, identity, city, mobile, agent_code):
        url = '/debt/staff/debt/agent-data'
        data = {
            # 1：业绩由高到底 2：业绩由底到高 3：创建时间由近到远 4：创建时间由远到近
            "sort_criteria": 4,
            # 0: 普通经纪人1:主管 2:经理
            "identity": identity,
            "city": city,
            "mobile": mobile,
            "agent_code": agent_code
        }
        result = HttpRequest.post_json(url, data, 'admin')
        if result["message"] == "success":
            logging.info('团队列表查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)团队列表查询失败的原因：' + result['message'])
            return result["message"]

    """
    地区分布
    """

    def area(self):
        url = '/debt/staff/debt/geographical-distribution'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2020-12-27",
            "type": 2
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布查询失败的原因：' + result['message'])
            return result["message"]

    """
    地区分布市搜索-二期
    """

    def query_city(self):
        url = '/debt/staff/debt/query-city'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2022-11-29",
            "city": 50
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]
    """
    地区分布省搜索-二期
    """

    def distribution(self):
        url = '/debt/staff/debt/distribution'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2022-11-29"
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('地区分布市查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)地区分布市查询失败的原因：' + result['message'])
            return result["message"]

    """
    数据概览-二期
    """

    def data_list(self):
        url = '/debt/staff/debt/data-list'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2022-11-29"
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('数据概览查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)数据概览查询失败的原因：' + result['message'])
            return result["message"]

    """
    数据概览线型图-二期
    """

    def line_plan(self):
        url = '/debt/staff/debt/line-plan'
        params = {
            "start_time": "2020-11-22",
            "end_time": "2022-11-29",
            "type": 10
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('数据概览线型图查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)数数据概览线型图查询失败的原因：' + result['message'])
            return result["message"]





if __name__ == '__main__':
    # # 数据中心 --- 经纪人数据-二期 筛选
    # AdminDataCentrol().query('', '', '', 'WR0001')
    # # 地区分布
    # AdminDataCentrol().area()
    # # 地区分布市搜索
    # AdminDataCentrol().query_city()
    # # 地区分布省搜索
    # AdminDataCentrol().distribution()
    # # 数据概览
    # AdminDataCentrol().data_list()
    # 数据概览线型图
    AdminDataCentrol().line_plan()