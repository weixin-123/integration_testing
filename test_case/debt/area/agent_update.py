#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : agent_update.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class AgentUpdata:
    """
    更新经纪人区域
    """

    def updata(self):
        url = '/debt/staff/agent/update'
        params = {
            "agent_id": 3,
            "province": "重庆",
            "city": "巴南",
            "city_code": "510700"
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('更新经纪人区域成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)更新经纪人区域失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print('经纪人区域更新结果为:', AgentUpdata().updata())
