#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : blacklist_list.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()

class BlackList:
    """
    黑名单列表
    """
    def black_list(self):
        url = '/debt/staff/debt/blacklist-list'
        result = HttpRequest.post_json(url, None, 'admin')
        if result["message"] == "success":
            logging.info('获取黑名单列表成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)黑名单获取失败失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print(BlackList().black_list())
    # ApplyAgent().agent_list()
