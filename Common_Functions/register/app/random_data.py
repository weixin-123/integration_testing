#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : random_data.py
"""
import random
import string


class Random_Data:
    # 随机生成电话号码
    @classmethod
    def random_phone(cls):
        num_start = ['134361']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 5))
        res = start + end
        return res


if __name__ == '__main__':
    print(Random_Data().random_phone())
