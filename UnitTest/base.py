# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-06 16:16
# @Author  : lidong@immusician.com
# @Site    :
# @File    : base.py

import requests
from UnitTest.settings import HOST, PORT, HEADERS


class BaseResponse:
    def __init__(self):
        pass


class BaseRequest:
    def __init__(self, host=None, port=None):
        self._host = host
        if not self._host:
            self._host = HOST

        self._port = port
        if not self._port:
            self._port = PORT

        self.__url = self._host + ":" + str(self._port)
        self.__headers = HEADERS

    def _check_url_and_headers(self, url, headers):
        url = self.__url + url

        if not headers:
            headers = self.__headers
        return url, headers

    def get(self, url, param=None, **kwargs):
        headers = kwargs.get("headers", None)
        url, headers = self._check_url_and_headers(url, headers)
        return requests.get(url, param, headers=headers, **kwargs)

    def post(self, url, json=None, **kwargs):
        headers = kwargs.get("headers", None)
        url, headers = self._check_url_and_headers(url, headers)
        return requests.post(url, json=json, headers=headers)

    def run(self):
        dir_list = self.__dir__()
        for func in dir_list:
            if not func.startswith("_"):
                if func not in ["get", 'post', 'run']:
                    url, ret = getattr(self, func)()
                    # self._show_data(func, url, ret)

    @staticmethod
    def _show_data(func_name, url, response):
        print("*"*10, func_name, "*"*10)
        print("url: ", url)
        print("status: ", response.status_code)
        print("json: ", response.json())
        print("")


if __name__ == '__main__':
    BaseRequest().run()
