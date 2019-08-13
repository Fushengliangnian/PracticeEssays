# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-09 14:35
# @Author  : lidong@immusician.com
# @Site    :
# @File    : ai-abtesting.py

import ujson
from UnitTest.base import BaseRequest


class AIABTesting(BaseRequest):
    def __init__(self):
        # TODO: 记得修改
        # super().__init__(host="http://api.iguitar.immusician.com", port=2525)
        super().__init__(port=22222)

    def upload_event_data(self):
        data = {
            "data": [
                {
                    "event_id": "5d494b8e191e7529d62b4add",
                    "uid": 1,
                    "create_time": 10,
                    "item_id": '1',
                    "item_type": 1,
                    "duration": None
                },
                {
                    "event_id": "5d494b8e191e7529d62b4add",
                    "uid": 1,
                    "create_time": 10,
                    "item_id": '1',
                    "item_type": 1,
                    "duration": None
                },
                {
                    "event_id": "5d494b8e191e7529d62b4add",
                    "uid": 1,
                    "create_time": 10,
                    "item_id": '1',
                    "item_type": 1,
                    "duration": None
                },
            ]
        }
        # data = {"data": "a"}
        url = "/v3/abtesting/upload_event_data/"
        ret = self.get(url, json=data)
        self._show_data("upload_event_data", url, ret)

    def get_all_event(self):
        url = "/v3/abtesting/get_all_event/"
        ret = self.get(url)
        self._show_data("get_all_event", url, ret)

    def create_event(self):
        data = {
            "event_name": "点击 vip特权 按钮",
            "event_type": 1,
            "event_need_params": {
                "item_id": {
                    "required": False,
                    "value_type": "str",
                    "description": "该类型的id",
                    "default": ""
                },
                "item_type": {
                    "required": True,
                    "value_type": "int",
                    "description": "类型(按钮)",
                    "default": 4
                },
                "event_id": {
                    "required": True,
                    "value_type": "str",
                    "description": "当前事件id"
                },
                "create_time": {
                    "required": True,
                    "value_type": "int",
                    "description": "创建时间"
                },
                "uid": {
                    "required": True,
                    "value_type": "int",
                    "description": "用户id"
                },
                "duration": {
                    "required": False,
                    "value_type": "int",
                    "description": "时长"
                },
            }
        }
        url = "/v3/abtesting/create_event/"
        ret = self.post(url, json=data)
        self._show_data("create_event", url, ret)

    def upload_event_data_single(self):
        data = {
            "event_id": "5d494b8e191e7529d62b4add",
            "uid": 1,
            "create_time": 10,
            "item_id": "",
            "item_type": 1,
            # "duration": None
        }
        url = "/v3/abtesting/upload_event_data/"
        ret = self.get(url, json=data)
        self._show_data("upload_event_data_single", url, ret)


if __name__ == '__main__':
    # AIABTesting().run()
    AIABTesting().create_event()
    # AIABTesting().get_all_event()
    # AIABTesting().upload_event_data()
    AIABTesting().upload_event_data_single()
