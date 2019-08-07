# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-06 16:33
# @Author  : lidong@immusician.com
# @Site    :
# @File    : abtesting.py
from UnitTest.base import BaseRequest


class ABTestingTest(BaseRequest):
    def __init__(self):
        super().__init__()

    def upload_event_data(self):
        data = {"data": [
            {
                "event_id": "1",
                "uid": 1,
                "create_time": 10,
                "item_id": '1',
                "item_type": 1
            },
            {
                "event_id": "1",
                "uid": 1,
                "create_time": 10,
                "item_id": '1',
                "item_type": 1
            },
            {
                "event_id": "1",
                "uid": 1,
                "create_time": 10,
                "item_id": '1',
                "item_type": 1
            },
        ]}
        url = "/v1/upload/event/info"
        ret = self.get(url, json=data)
        return url, ret

    def get_all_event(self):
        url = "/v1/get/event"
        ret = self.get(url)
        return url, ret


if __name__ == '__main__':
    ABTestingTest().run()
