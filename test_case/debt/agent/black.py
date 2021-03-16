#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : black.py
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
    BlacklistCreate().black_add(13436183072)
    # ApplyAgent().agent_list()
