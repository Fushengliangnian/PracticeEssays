from ServiceRegistry.protos import service_registry_pb2_grpc as pb2_grpc
from ServiceRegistry.protos import service_registry_pb2 as pb2
from ServiceRegistry.config.connections import RedisConn4


class BaseService(pb2_grpc.ServiceRegistryServicer):
    pb2 = pb2
    redis_conn = RedisConn4.instance().conn
