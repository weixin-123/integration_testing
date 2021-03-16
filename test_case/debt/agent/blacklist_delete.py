#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : blacklist_delete.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()

class BlackListDelete:
    """
    删除黑名单
    """

    def black_delete(self, phone):
        url = '/debt/staff/debt/blacklist-delete'
        params = {
            "member_mobile": [phone],
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('删除黑名单成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)黑名单移除失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    BlackListDelete().black_delete(13436182072)
    # ApplyAgent().agent_list()
