#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : upload_merchant.py
"""
import json
from faker import Faker
<<<<<<< HEAD
from Common_Functions.login_step.login_app import LoginApp
from test_case.car_v2.buy_car.use_sql import UseSql
=======
from test_case.car_v2.login_step.login_app import LoginApp
from test_case.car_v2.login_step.use_sql import UseSql
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587

f = Faker('zh_CN')
from common.request import HttpRequest

<<<<<<< HEAD
from Common_Functions.register.store_app.random_data import Random_Data
=======
from test_case.car_v2.login_step.random_data import Random_Data
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
from common.log_color import LogingColor

city_code = Random_Data().random_city_code()
business_license = Random_Data().random_business_license()
card_front = Random_Data().random_card_image("card_front")
card_behind = Random_Data().random_card_image("card_behind")
logging = LogingColor()


class UploadMerchant:

    # def __init__(self):
    #     # self.merchant = Random_Data().random_merchant()
    #     self.merchant = '服务中心'

<<<<<<< HEAD
    def upload_merchant(self, merchant, phone, name):
        # 调用登录会员的电话号码
        phone = LoginApp().login_app(phone)
=======
    def upload_merchant(self, merchant):
        # 调用登录会员的电话号码
        phone = LoginApp().login_app(13436137948)
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        # logging.info("登录的手机号为：" + phone)
        """
        登录销巴APP
        """
        logging.info("你注册的商家类型是:" + merchant)
<<<<<<< HEAD
        if merchant == "个人" or merchant == "二手车经销商":
            # 调用接口
            url = "/car-v2/member/merchant/individualSeller"
            if merchant == "个人":
=======
        if merchant == "普通个人" or merchant == "个人门店":
            # 调用接口
            url = "/car-v2/member/merchant/individualSeller"
            if merchant == "普通个人":
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                data = {
                    "address": f.street_address(),
                    "card_front": card_front,
                    "card_behind": card_behind,
                    "city_code": json.dumps(city_code),
                    "expire_at": f.date_between(start_date=300, end_date=600),
<<<<<<< HEAD
                    # "name": f.first_name(),
                    "name": name,
=======
                    "name": f.first_name(),
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                    "phone_number": phone,
                    "type": merchant,
                    "credentials_num": f.ssn()
                }
                result = HttpRequest.post(url, data, service_name="app")
                if result["message"] == "success":
                    logging.info('%s提交成功，等待审核(*^▽^*)' % merchant)
                    return phone
                else:
                    logging.error('(ಥ﹏ಥ)%s提交失败的原因：' % merchant + result['message'])
                    return result["message"]
            else:
                """
<<<<<<< HEAD
                二手车经销商
=======
                个人门店
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                """
                data = {
                    "address": f.street_address(),
                    "business_license[]": business_license,
                    "city_code": json.dumps(city_code),
                    "company_full_name": f.company(),
                    "company_short_name": f.company_prefix(),
                    "credentials_num": f.ssn(),
                    "card_front": card_front,
                    "card_behind": card_behind,
                    "credentials_type": f.company(),
                    "end_business_at": f.date_between(start_date=300, end_date=600),
<<<<<<< HEAD
                    # "name": f.first_name(),
                    "name": name,
=======
                    "name": f.first_name(),
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                    "phone_number": f.phone_number(),
                    "start_business_at": f.past_date(),
                    "type": merchant,
                    "establishment_at": f.past_date()
                }
                result = HttpRequest.post(url, data, service_name="app")

                if result["message"] == "success":
                    logging.info('%s提交成功，等待审核(*^▽^*)' % merchant)
                    return phone
                else:
                    logging.error('(ಥ﹏ಥ)%s提交失败的原因：' % merchant + result['message'])
                    return result["message"]
        else:
            """
            申请直营店/服务中心/商家/代理人
            """
            # 调用接口
            url = "/car-v2/member/merchant/professionalSeller"
<<<<<<< HEAD
            if merchant == "直营店" or merchant == "服务中心":
=======
            if merchant == "直营店" or merchant == "服务中心" or merchant == "商家":
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                params = {
                    "address": f.street_address(),
                    "business_license": business_license,
                    "city_code": json.dumps(city_code),
                    "company_full_name": f.company(),
                    "company_short_name": f.company_prefix(),
                    "credentials_num": f.ssn(),
                    "credentials_type": f.company(),
                    # "end_business_at": f.date_between(start_date=300, end_date=600),
                    "end_business_at": "2022-01-01",
                    "establishment_at": "2016-12-01",
<<<<<<< HEAD
                    # "name": f.first_name(),
                    "name": name,
=======
                    "name": f.first_name(),
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                    "phone_number": f.phone_number(),
                    "start_business_at": "2019-12-01",
                    "type": merchant,
                }
                temp_data = json.dumps(params)
                result = HttpRequest.post(url, temp_data, service_name="app")
                if result["message"] == "success":
                    logging.info('%s提交成功，等待审核(*^▽^*)' % merchant)
                    return phone
                else:
                    logging.error('(ಥ﹏ಥ)%s提交失败的原因：' % merchant + result['message'])
                    return result["message"]
            else:
                """
<<<<<<< HEAD
                申请代理人/汽车专员
=======
                申请代理人
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                """
                data = {
                    "address": f.street_address(),
                    "card_front": card_front,
                    "card_behind": card_behind,
                    "city_code": json.dumps(city_code),
                    "credentials_num": f.ssn(),
                    "expire_at": f.date_between(start_date=300, end_date=600),
<<<<<<< HEAD
                    # "name": f.first_name(),
                    "name": name,
=======
                    "name": f.first_name(),
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
                    "phone_number": f.phone_number(),
                    "type": merchant,
                }
                result = HttpRequest.post(url, data, service_name="app")
                if result["message"] == "success":
                    logging.info('%s提交成功，等待审核(*^▽^*)' % merchant)
                    return phone
                else:
                    logging.error('(ಥ﹏ಥ)%s提交失败的原因：' % merchant + result['message'])
                return result["message"]

    def merchant_approved(self, merchant):
        """
        商家审核通过
        :return:
        """
        phone = UploadMerchant().upload_merchant(merchant)
        merchant_id = UseSql().use_sql_select_two(phone)
        # 调用接口
        url = "/car-v2/staff/merchant/franchisee/approved"
        data = {"id": merchant_id}
        response = HttpRequest.post(url, data, service_name="admin")
        # response_json = response.json()
        if response["message"] == "success":
            logging.info('电话号码为%s：%s审核成功(*^▽^*)' % (phone, merchant))
        else:
            logging.error('(ಥ﹏ಥ)%s审核失败的原因：' % merchant + response['message'])
            return response["message"]


if __name__ == "__main__":
<<<<<<< HEAD
    # # 上传商家 --- 二手车经销商/个人
    UploadMerchant().upload_merchant('个人', 13436183072, "阿奴")
    # # 上传商家 直营店/服务中心/汽车专员/代理人
    # UploadMerchant().upload_merchant('直营店', 13436183072, "阿奴")

    # 商家审核通过


=======
    print(UploadMerchant().merchant_approved('代理人'))
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
