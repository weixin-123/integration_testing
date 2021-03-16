#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2021/03/01
@File    : register_shop.py
"""
import json

from faker import Faker
from common.log_color import LogingColor

from common.read_user_config import ReadUserConfig
from common.request import HttpRequest
from Common_Functions.login_step.login_store_app import LoginApp
f = Faker('zh_CN')
logging = LogingColor()

read_user = ReadUserConfig()


class RegisterShop:

    def register_shop(self, shop_name,  phone, name, id_card, certificate_no):
        """
        注册线下店铺
        :param phone:
        :return:
        """
        LoginApp().login_store_app(phone)
        register_shop_url = "/offshop/store/shop/o2o-register"
        params = {
            "shop": {
                # #0：就是没有 1：门店自提，2：服务核销 示例：[1,2]
                "send_type": "2",
                # 1：零售，2：餐饮
                "shop_type": 1,
                "shop_name": shop_name,
                "tel": phone,
                # 联系人
                "contact": name,
                "customer_service_tel": 88888888,
                # 店铺一级分类
                "top_o2o_category": 271,
                "business_hours_start": "16:28",
                "business_hours_end": "21:28",
                # 省市区
                "province": "110000",
                "city": "110100",
                "district": "110114",
                # 备注：详细地址
                "address": "北京市昌平区南口镇山羊洼",
                # 经度
                "longitude": 116.0464,
                # 纬度
                "latitude": 40.284407,
                "area_name": "北京市 北京市 昌平区",
                "areaId": [1, 2, 13],
                "logo": "http://shop-qiniu.shall-buy.com/shop-20210311103551377378.jpg",
                "face": "http://shop-qiniu.shall-buy.com/shop-20210311103651632938.jpg",
                "condition": ["http://shop-qiniu.shall-buy.com/shop-20210311103654621689.jpg"]
                },
            # # 主营产品
            # "main_product": "123123",
            "certificate": [
                {
                    # 1法人证件 2 3其他
                    "type": 1,
                    # 法人名称
                    "representative_name": name,
                    #
                    "id_card_type": 1,
                    # 身份证号
                    "certificate_no": id_card,
                    # 过期日期，为空表示长期或永久
                    "expire_date": "2025-11-27",
                    # 只有type为1的时候才这样传
                    "image": [
                    {
                        "url": "http://qualification-qiniu.shall-buy.com/qualification-20210311105124149393.jpg",
                        "remark": "证件正面照"
                    }, {
                        "url": "http://qualification-qiniu.shall-buy.com/qualification-20210311105126338372.jpg",
                        "remark": "证件反面照"
                    }]
                },
                {
                    # 商家营业执照
                    "type": 2,
                    "certificate_no": certificate_no,
                    "expire_date": "2037-06-20",
                    "image": "http://qualification-qiniu.shall-buy.com/qualification-20210311104844971129.jpg"
                }
                ]
        }
        # logging.info("请求URL：" + register_shop)
        # logging.info("请求参数:" + str(params))
        # 将str格式转化成json格式
        temp_params=json.dumps(params)
        result = HttpRequest.post(register_shop_url, temp_params, "store_app")
        # result_json = result.json()
        if result["message"] == "success":
            logging.info('注册销巴线下店铺成功(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)注册销巴线下店铺失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    # shop_name店铺名 phone电话 name联系人 id_card身份证号 certificate_no营业执照
    res = RegisterShop().register_shop("伊谧零食铺", 13436189615, "伊谧", '31010119840307046X', "91532522MA6KR3J45f")

