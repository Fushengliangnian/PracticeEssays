import time
from concurrent import futures

import grpc

from ServiceRegistry.protos import service_registry_pb2_grpc as pb2
from ServiceRegistry.service.registry import RegistryService
from ServiceRegistry.config.settings import ONE_DAY_IN_SECONDS, PORT


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2.add_ServiceRegistryServicer_to_server(RegistryService(), server)
    server.add_insecure_port('[::]:%s' % PORT)

    server.start()
    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
