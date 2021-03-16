#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : blacklist_create.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()

class BlacklistCreate:
    """
    添加黑名单
    """

    def black_add(self, phone):
        url = '/debt/staff/debt/blacklist-create'
        params = {'member_mobile':[phone],}

        result = HttpRequest.post_json(url, params, 'admin')
        print(result)

        # print(result)
        # res = json.loads(result.text)
        # print(res)
        if result["message"] == "success":
            logging.info('加入黑名单(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)加入黑名单失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    BlacklistCreate().black_add(13436182072)
    # ApplyAgent().agent_list()
