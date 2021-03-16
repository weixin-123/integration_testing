#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/14
@File    : content_setting.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class ContentSetting:
    """
    内容设置
    """

    def list(self):
        url = '/debt/staff/content-setting/list'
        result = HttpRequest.post_json(url, None, 'admin')
        if result["message"] == "success":
            logging.info('内容配置列表查询成功(*^▽^*)')
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ)配置列表查询失败的原因：' + result['message'])
            return result["message"]

    def edit(self):
        url = '/debt/staff/content-setting/edit'
        params = {
            'id': 6,
            'title': '什么是解债',
            'details': "说明书"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('编辑配置成功(*^▽^*)')
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ)编辑配置失败的原因：' + result['message'])
            return result["message"]

    def detail(self):
        url = '/debt/staff/content-setting/detail'
        params = {
            'id': 6
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            return result["message"]
        else:
            logging.error('(ಥ﹏ಥ) 财务审核失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    ContentSetting().detail()
