# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-09 14:35
# @Author  : lidong@immusician.com
# @Site    :
# @File    : ai-abtesting.py

import ujson
import time
from UnitTest.base import BaseRequest


class AIABTesting(BaseRequest):
    def __init__(self):
        # TODO: 记得修改
        # super().__init__(host="http://58.87.125.111", port=2525)
        super().__init__(host="http://api.iguitar.immusician.com", port=2525)
        # super().__init__(port=22222)

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
            "event_name": "点击 vip特权  按钮",
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
        data2 = {
            "event_name": "尤克里里点击 vip特权  按钮",
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
        lesson_data = {
            "event_name": "点击lesson事件",
            "event_type": 1,
            "event_need_params": {
                "item_id": {
                    "required": False,
                    "value_type": "str",
                    "description": "该类型的id",
                },
                "item_type": {
                    "required": True,
                    "value_type": "int",
                    "description": "类型(lesson)",
                    "default": 2
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
                "other": {
                    "required": False,
                    "value_type": "dict",
                    "description": "其他参数"
                }
            }
        }
        course_data = {
            "event_name": "点击course事件",
            "event_type": 1,
            "event_need_params": {
                "item_id": {
                    "required": True,
                    "value_type": "str",
                    "description": "该类型的id",
                    "default": ""
                },
                "item_type": {
                    "required": True,
                    "value_type": "int",
                    "description": "类型(course)",
                    "default": 1
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
                "other": {
                    "required": False,
                    "value_type": "dict",
                    "description": "其他参数"
                }
            }
        }
        song_data = {
            "event_name": "点击 曲谱事件",
            "event_type": 1,
            "event_need_params": {
                "item_id": {
                    "required": False,
                    "value_type": "str",
                    "description": "曲谱id",
                    "default": ""
                },
                "item_type": {
                    "required": True,
                    "value_type": "int",
                    "description": "类型(曲谱)",
                    "default": 8
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
                "other": {
                    "required": False,
                    "value_type": "dict",
                    "description": "其他参数"
                }
            }
        }
        url = "/v3/abtesting/create_event/"
        ret = self.post(url, json=lesson_data)
        self._show_data("create_event", url, ret)

    def upload_event_data_single(self):
        data = {
            "event_id": "5d5a1a0dc938cda633d5a20f",
            "uid": 0,
            "create_time": int(time.time()),
            "item_id": "https://www.baidu.com",
            "item_type": 6,
            # "duration": None
        }
        data2 = {
            "event_id": "5d5a1a0dc938cda633d5a210",
            "uid": 0,
            "create_time": int(time.time()),
            "item_id": "小星星",
            "item_type": 4,
            # "duration": None
        }
        data_song = {
            "event_id": "5d661772191e75fe93125f55",
            "item_id": "247",
            "create_time": "1566973150",
            "item_type": "1",
            "other": ujson.dumps({"instrument_type": "ukulele"}),
            "uid": "1"
        }
        url = "/v3/abtesting/upload_event_data/"
        ret = self.get(url, json=data2)
        self._show_data("upload_event_data_single", url, ret)

    def get_project_data(self):
        url = "/v1/get_project_data"
        data = {
            "project_id": "5d553aa9c938cda633d5a20b"
        }
        ret = self.get(url, param=data)
        self._show_data("get_project_data", url, ret)

    def get_course(self):
        url = "/v1/get_course"
        ret = self.get(url)
        self._show_data("get_course", url, ret)

    def create_course(self):
        url = "/v1/create_course"
        ret = self.post(url, json={"course_id": 14, "course_name": "未命名"})
        self._show_data("create_course", url, ret)

    def get_all_indicator(self):
        url = "/v1/get_all_indicator"
        ret = self.get(url)
        self._show_data("get_all_indicator", url, ret)

    def get_item_list(self):
        url = "/v1/get_item_list"
        data = {"item_type": 5}
        ret = self.get(url, param=data)
        self._show_data("get_item_list", url, ret)

    def create_indicator(self):
        url = "/v3/create_indicator"
        data = {
            "name": "事件(需绑定项目id) -- 统计点击总数",
            "db_name": "jita",
            "collection_name": "v3_event_info",
            "select_args": {
                "item_id": {
                    "description": "该事件下所绑定的id",
                    "required": True,
                    "value_type": "str",
                    # "is_show_list": True,
                    # "item_type": 5
                },
                "event_id": {
                    "description": "事件id",
                    "required": True,
                    "value_type": "str",
                    "is_show_list": True,
                    "item_type": 7
                }
            },
            "is_ratio": False,
            "need_way": {
                "compute_total": [
                    "create_time"
                ]
            },
            "show_data": {}
        }

        data2 = {
            "name": "事件(无需绑定项目id) -- 统计点击总数",
            "db_name": "jita",
            "collection_name": "v3_event_info",
            "select_args": {
                "event_id": {
                    "description": "事件id",
                    "required": True,
                    "value_type": "str",
                    "is_show_list": True,
                    "item_type": 7
                }
            },
            "is_ratio": False,
            "need_way": {
                "compute_total": [
                    "create_time"
                ]
            },
            "show_data": {}
        }

        course_ind = {
            "name": "统计单个用户所有课程点击信息",
            "db_name": "jita",
            "collection_name": "v3_event_info",
            "select_args": {
                "uid": {
                    "description": "用户id",
                    "required": True,
                    "value_type": "int"
                },
                "event_id": {
                    "description": "event id",
                    "required": False,
                    "value_type": "str",
                    "default": "5d662496ea56aa000c5ffd95"
                }
            },
            "is_ratio": False,
            "need_way": {
                "aggr_course_by_event_id_and_uid": [
                    "create_time"
                ]
            },
            "show_data": {
                "info_list": "course_by_aggregation"
            }
        }   # 120: 5d6dd680ea56aa037fe818ef
        score_ind = {
            "name": "统计单个用户所有曲谱点击信息",
            "collection_name": "v3_event_info",
            "select_args": {
                "event_id": {
                    "default": "5d6624b7ea56aa000b050848",
                    "required": False,
                    "value_type": "str",
                    "description": "event id"
                },
                "uid": {
                    "required": True,
                    "value_type": "int",
                    "description": "用户id"
                }
            },
            "db_name": "jita",
            "is_ratio": False,
            "need_way": {
                "aggr_score_by_event_id_and_uid": [
                    "create_time"
                ]
            },
            "show_data": {
                "info_list": "score_by_aggregation"
            }}   # 120: 5d6dd659ea56aa000d9ffed3
        ret = self.post(url, json=course_ind)
        self._show_data("create_indicator", url, ret)

    def get_activity(self):
        url = "/v3/get_activity"
        ret = self.get(url)
        self._show_data("get_activity", url, ret)

    def get_single_user_statics_info(self):
        url = "/v3/get_single_user_statics_info"
        course_id = "5d663dfc92b157c5b289d69e"
        course_id_111 = "5d663bcf8538bacf6454666c"
        song_id = "5d6c80e592b157c5b289d69f"
        song_id_111 = "5d6c89444a1dd4000ac9146b"
        # params = {"uid": 400368173, "indicator_id": course_id_111}
        params = {"uid": 400368173, "indicator_id": song_id_111}
        # params = {"uid": 405751145, "indicator_id": song_id_111}
        ret = self.get(url, param=params)
        self._show_data("get_single_user_statics_info", url, ret)


if __name__ == '__main__':
    # AIABTesting().run()
    # AIABTesting().create_event()
    # AIABTesting().get_all_event()
    # AIABTesting().upload_event_data()
    # AIABTesting().upload_event_data_single()
    # AIABTesting().get_project_data()
    # AIABTesting().get_course()
    # AIABTesting().create_course()
    # AIABTesting().get_all_indicator()
    # AIABTesting().get_item_list()
    AIABTesting().create_indicator()
    # AIABTesting().get_activity()
    # AIABTesting().get_single_user_statics_info()
