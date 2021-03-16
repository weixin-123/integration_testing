#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/20
@File    : updata_debt_time.py
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 09:28
# @Author  : lijian
# @File    : update_time.py
# @Software: PyCharm
from common.log_color import LogingColor
from test_case.debt.update_time.query_debt_sql import UseSql
from test_case.debt.update_time.debt_time_change import TimeChange

log = LogingColor()


class UpdateTime:
    # 结算日期：每月改为相同的一天
    def update_every_day(self):
        temp_list = []
        i=0
        for data in range(36):
            data = UseSql().use_sql_select_order(39)[i]
            temp_data = data.strftime("%Y-%m-%d")
            TimeChange().change_day_time_format()
            temp_list.append(temp_data)
        print(temp_list)








if __name__ == "__main__":
    UpdateTime().update_every_day()
