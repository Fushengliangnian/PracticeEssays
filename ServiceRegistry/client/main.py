# -*- coding: utf-8 -*-
import grpc

from ServiceRegistry.protos import service_registry_pb2_grpc as pb2_grpc
from ServiceRegistry.protos import service_registry_pb2 as pb2


def run():
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = pb2_grpc.ServiceRegistryStub(channel)
        request = pb2.Request(addr="192.168.1.120:8888", name="120测试机", desc="测试玩")
        response = stub.RegServer(request)
        print(response.msg)
        print(response.error)
        print(response.code)


if __name__ == '__main__':
    run()
