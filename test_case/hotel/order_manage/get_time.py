#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/01/12
@File    : get_time.py
"""
import datetime

class GetTime:
    """
    获取需要的时间
    """
    def change_day_time_format(self, days):
        now_time = datetime.datetime.now()
        temp_time = now_time + datetime.timedelta(days=days)
        return temp_time.strftime('%Y-%m-%d')

if __name__ == "__main__":
    print(GetTime().change_day_time_format(0))