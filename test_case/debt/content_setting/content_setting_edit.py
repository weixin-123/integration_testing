#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : content_setting_edit.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class ContentSetting:
    """
    编辑内容配置
    """

    def edit(self):
        url = '/debt/staff/content-setting/edit'
        params = {
            "id": 3,
            "title": "债权人",
            "details": "说明书"
        }
        result = HttpRequest.post(url, params, 'admin')
        if result["message"] == "success":
            logging.info('编辑配置成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)编辑配置失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    # print('内容配置列表:', ContentSetting().list())
    ContentSetting().edit()
