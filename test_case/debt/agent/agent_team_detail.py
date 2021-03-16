#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/12/18
@File    : agent_team_detail.py
"""
from common.log_color import LogingColor
from common.request import HttpRequest
from Common_Functions.login_step.login_app import LoginApp

logging = LogingColor()


class AgentTeamList:
    """
    团队列表-二期
    """

    def list(self):
        url = '/debt/member/agent/agent-list'
        data = {
            "size": 10,
            "page": 1
        }
        result = HttpRequest.post_json(url, data, 'app')
        if result["message"] == "success":
            logging.info('团队列表查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)团队列表查询失败的原因：' + result['message'])
            return result["message"]

    """
    团队搜索-二期
    """

    def query(self):
        url = '/debt/member/agent/team-query'
        data = {
              "condition":"WR0003"
        }
        result = HttpRequest.post_json(url, data, 'app')
        if result["message"] == "success":
            logging.info('团队列表查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ)团队列表查询失败的原因：' + result['message'])
            return result["message"]

    """
    经纪人团队-二期
    """

    def agent_team(self):
        url = '/debt/member/agent/team'
        result = HttpRequest.post_json(url, None, 'app')
        if result["message"] == "success":
            logging.info(' 经纪人团队查询成功(*^▽^*)')

        else:
            logging.error('(ಥ﹏ಥ) 经纪人团队查询失败的原因：' + result['message'])
            return result["message"]

if __name__ == '__main__':
    # # 团队列表
    # AgentTeamList().list()
    # # 团队搜索
    # AgentTeamList().query()
    # 经纪人团队信息
    LoginApp().login_app(13436167502)
    AgentTeamList().agent_team()


