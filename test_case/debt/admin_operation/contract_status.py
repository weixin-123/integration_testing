#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/10
@File    : contract_status.py
"""
from test_case.debt.admin_operation.dev_use_sql import DevDebtData
from common.log_color import LogingColor
from common.request import HttpRequest

logging = LogingColor()


class Contract:
    """
    合同审批
    """

    def contract_pass(self, id):
        url = '/contract/staff/contract/change/status'
        params = {
            "contract_id" : id,
            "contract_status": 1
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('合同审批通过(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 合同审批失败的原因：' + result['message'])
            return result["message"]

    """
    合同审核驳回
    """
    def reject(self, id):
        url = '/contract/staff/contract/change/status'
        params = {
            "contract_id": id,
            "contract_status": -1,
            "rejected_reason": "阿拉啦啦啦"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info(' 合同审核驳回通过(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 合同审核驳回失败的原因：' + result['message'])
            return result["message"]

    """
    合同审核撤回
    """

    def withdraw(self, id):
        url = '/contract/staff/contract/change/status'
        params = {
            "contract_id": id,
            "contract_status": -2,
            "rejected_reason": "重新发布吧"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('合同审核撤回通过(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 合同审核撤回失败的原因：' + result['message'])
            return result["message"]

    """
     合同审核失效
    """

    def efficacy(self, id):
        url = '/contract/staff/contract/change/status'
        params = {
            "contract_id": id,
            "contract_status": -3
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('合同失效啦(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ) 合同失效失败的原因：' + result['message'])
            return result["message"]

    """
    合同审核作废
    """

    def void(self, id):
        url = '/contract/staff/contract/change/status'
        params = {
            "contract_id": id,
            "contract_status": -4
            # "rejected_reason": "作废了"
        }
        result = HttpRequest.post_json(url, params, 'admin')
        if result["message"] == "success":
            logging.info('合同审核作废通过(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ) 合同审核作废失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    id = 49
    contract_id = DevDebtData().query_contract(id)[0][0]
    # order_id = PublishOrder().publish()
    # 合同通过
    Contract().contract_pass(contract_id)