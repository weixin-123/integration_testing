#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/09
@File    : content_setting_list.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()

class ContentSetting:
    """
    获取内容配置列表
    """

    def list(self):
        url = '/debt/staff/content-setting/list'
        result = HttpRequest.post(url, None, 'admin')

        # print(result)
        # res = json.loads(result.text)
        # print(res)
        if result["message"] == "success":
            logging.info('内容配置列表查询成功(*^▽^*)')
            return result['data']

        else:
            logging.error('(ಥ﹏ಥ)配置列表查询失败的原因：' + result['message'])
            return result["message"]


if __name__ == '__main__':
    print('内容配置列表:', ContentSetting().list())
