#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/05
@File    : learning.py
"""
<<<<<<< HEAD
from faker import Faker
f = Faker('zh_CN')
import datetime


# print('abc')
# print("你好世界")
# print("你好呀  宝宝亲")
if __name__ == "__main__":
    # print(f.date_time('now'))
    # print(datetime.datetime.now())
    now_time = datetime.datetime.now()
    temp_time = now_time.strftime("%Y-%m-%d")
    print(temp_time)
=======
print('abc')
print("你好世界")
print("你好呀  宝宝亲")
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
