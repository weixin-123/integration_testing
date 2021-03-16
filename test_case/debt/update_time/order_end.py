#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/11
@File    : order_end.py
"""
from test_case.debt.update_time.query_debt_sql import UseSql
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()
<<<<<<< HEAD
today = '2020-12-23 00:00:00'
=======
today = '2020-12-11 00:00:00'
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587


class OrderTime:
    def test_time(self):
<<<<<<< HEAD
        # UseSql().use_sql_execute_time(order_id, today)
=======
        UseSql().use_sql_execute_time(54, today)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        url = '/debt/inner/task/repayment'
        result = HttpRequest.post_json(url, None, 'inner')
        if result["message"] == "success":
            logging.info('定时任务已开启，已经完成还款(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 定时任务失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    OrderTime().test_time()
