# -*- coding: utf-8 -*-
import json

from ServiceRegistry.service.base_service import BaseService


class RegistryService(BaseService):
    def RegServer(self, request, context):
        addr = request.addr
        name = request.name
        desc = request.desc
        key = "RegistryService:%s" % addr
        if self.redis_conn.get(key):
            print(locals())
            return self.pb2.Response(error=True, msg="当前地址已存在", code=1)
        self.redis_conn.set(key, value=json.dumps({"addr": addr, "name": name, "desc": desc, "code": 200}))
        return self.pb2.Response(error=False, msg="ok", code=200)

    def LogoutService(self, request, context):
        addr = request.addr
        key = "RegistryService:%s" % addr
        value = self.redis_conn.get(key)
        if not value:
            return self.pb2.Response(error=True, msg="当前地址不存在", code=2)
        value_dict = json.loads(value)
        value_dict["code"] = 201
        self.redis_conn.set(key, value=json.dumps(value_dict))
        return self.pb2.Response(error=False, msg="注销成功", code=200)

    def send_gateway(self):
        """
        向网关实时发送更新后的路由
        :return:
        """
        pass
