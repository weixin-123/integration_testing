#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/16
@File    : get_new_car_series.py
"""
import json
import random
from faker import Faker

from common.request import HttpRequest
from common.log_color import LogingColor

f = Faker('zh_CN')

logging = LogingColor()


class GetNewCarSeries:
    """
<<<<<<< HEAD
    通过品牌id获取车系  车系选择
    """
    def get_car_series(self, brand_id):
        url = "/car-v2/index/buy-car/car_series/%s" % brand_id
        """
        %s替换表示brand_id是传参数据
        """
        result = HttpRequest.get(url, None, 'inner')
        if result["message"] == "success":
            logging.info('车系选择成功，请选择你喜欢的车型吧')
=======
    通过品牌id获取车系
    """

    def get_car_series(self, brand_id):
        url = "/car-v2/member/buy-car/car_series/%s" % brand_id
        """
        %s替换表示brand_id是传参数据
        """
        result = HttpRequest.get(url, None, service_name="app")
        if result["message"] == "success":
            logging.info('品牌选择成功，请选择你喜欢的车系吧')
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
            result_data = result['data']['list'][0]['list']
            temp_data_list = []
            for i in result_data:
                data = i
                temp_data = data['id']
                # print("temp_data:",temp_data)
                temp_data_list.append(temp_data)
                # temp_data=result['data']['list'][0]['list'][i]['id']
            brand_model_id = random.choice(temp_data_list)
            return brand_model_id

        else:
            logging.error('品牌选择失败的原因：' + result['message'])
            result["message"] = json.dumps("message")
            return result["message"]

<<<<<<< HEAD
    def get_car_brand_model_version(self, brand_id):
=======
    def car_detail(self, brand_id):
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
        """
        获取新车详情
        :return:
        """
<<<<<<< HEAD
        # 选择你喜欢的车系
        brand_model_id = GetNewCarSeries().get_car_series(brand_id)
        # 选择你喜欢的车型
        url = "/car-v2/index/buy-car/version_list/%s" % brand_model_id
        result = HttpRequest.get(url, None, 'inner')
        if result["message"] == "success" and result["data"]["list"] != []:
            brand_model_version = random.choice(result["data"]["list"])
            print("brand_model_version", brand_model_version)
            logging.info('车型选择成功')
            # guid_price = result['data']['brand']['guid_price']
            # # print("guid_price", guid_price)
            # if guid_price != '暂无预售价' or result'':
            #     result_list = result['data']['list'][0]["list"]
            #     print('result_list:', result_list)
            #     total = len(result_list)
            #     # print("total的值为：", total)
            #     if total >= 1:
            #         data = random.randint(1, total)
            #         # print(data)
            #         result_data = result['data']['list'][0]['list'][data - 1]
            #         # print("result_data", result_data)
            #         # 车辆标题图 "http://car-goods.qiniudns.shall-buy.com/brand_model_versions_52769_0.jpg",
            #         result_first_image = result_data['first_image']
            #         # 品牌型号id 5
            #         result_brand_model_id = result_data['brand_model_id']
            #         # 品牌于车系 "奥迪Q2L"
            #         result_brand_model = result_data['brand_model']['name']
            #         # 汽车级别
            #         result_category_type = result_data['category_type']
            #         # 品牌型号版本名称
            #         result_name = result_data['name']
            #         # 车类型id
            #         result_standard_type_id = result_data['standard_type_id']
            #         # 官方指导价
            #         result_official_price = result_data['official_price']
            #         # print("result_data：", result_name)
            #         # print("result_first_imageme:", result_first_image)
            #         # car_id
            #         result_car_id = result_data['id']
            #         temp_car_data = {"image": result_first_image, "brand_model_id": result_brand_model_id,
            #                          "brand_model": result_brand_model, "car_rank": result_category_type,
            #                          "car_versions": result_name, "standard_type_id": result_standard_type_id,
            #                          "car_name": result_name, "car_id": result_car_id,
            #                          "official_price": result_official_price}
            #         # print(temp_car_data)
            #         if result_standard_type_id == '':
            #             GetNewCarSeries().get_car_brand_model_version(1)
            #         else:
            #             return temp_car_data
        else:
            logging.info("---暂无预售价/无车型, 请重新选择你喜欢的车系进行购买吧！---")
            GetNewCarSeries().get_car_brand_model_version(brand_id)


    def car_old_detail(self, car_source_id):
        """
        获取二手车详情
        :return:
        """
        # 品牌详情
        url = "/car-v2/index/buy-car/second_hand_car/%s" % car_source_id
        result = HttpRequest.get(url, None, 'inner')
        if result["message"] == "success":
            logging.info('查询二手车官方指导价成功！！')
            return result['data']
        else:
            logging.info("---暂无预售价, 请重新选择你喜欢的车系进行购买吧！---")



if __name__ == "__main__":
    # 奥迪 1 阿斯顿
    # print(GetNewCarSeries().get_car_series(1))
    GetNewCarSeries().get_car_brand_model_version(1)
    # result=Get_Car_Series().car_detail(1)
    # data_dname=result['id']
    # data = GetNewCarSeries().car_old_detail(94)
    # print(data['images']['front'])
=======
        brand_model_id = GetNewCarSeries().get_car_series(brand_id)
        url = "/car-v2/member/buy-car/new_car/%s" % brand_model_id
        result = HttpRequest.get(url, None, service_name="app")
        if result["message"] == "success":
            print("result", result)
            logging.info('车系选择成功，请选择你喜欢的车型吧')
            guid_price = result['data']['brand']['guid_price']
            # print("guid_price", guid_price)
            if guid_price != '暂无预售价':
                result_list = result['data']['list'][0]["list"]
                total = len(result_list)
                # print("total的值为：", total)
                if total >= 1:
                    data = random.randint(1, total)
                    # print(data)
                    result_data = result['data']['list'][0]['list'][data - 1]
                    # print("result_data", result_data)
                    # 车辆标题图 "http://car-goods.qiniudns.shall-buy.com/brand_model_versions_52769_0.jpg",
                    result_first_image = result_data['first_image']
                    # 品牌型号id 5
                    result_brand_model_id = result_data['brand_model_id']
                    # 品牌于车系 "奥迪Q2L"
                    result_brand_model = result_data['brand_model']['name']
                    # 汽车级别
                    result_category_type = result_data['category_type']
                    # 品牌型号版本名称
                    result_name = result_data['name']
                    # 车类型id
                    result_standard_type_id = result_data['standard_type_id']
                    # 官方指导价
                    result_official_price = result_data['official_price']
                    # print("result_data：", result_name)
                    # print("result_first_imageme:", result_first_image)
                    # car_id
                    result_car_id = result_data['id']
                    temp_car_data = {"image": result_first_image, "brand_model_id": result_brand_model_id,
                                     "brand_model": result_brand_model, "car_rank": result_category_type,
                                     "car_versions": result_name, "standard_type_id": result_standard_type_id,
                                     "car_name": result_name, "car_id": result_car_id,
                                     "official_price": result_official_price}
                    # print(temp_car_data)
                    if result_standard_type_id == '':
                        GetNewCarSeries().car_detail(1)
                    else:
                        return temp_car_data
            else:
                logging.info("---暂无预售价, 请重新选择你喜欢的车系进行购买吧！---")
                GetNewCarSeries().car_detail(1)


if __name__ == "__main__":
    GetNewCarSeries().car_detail(1)
    # result=Get_Car_Series().car_detail(1)
    # data_dname=result['id']
>>>>>>> 52b7a54846e9aafd772c8167507825af985d6587
