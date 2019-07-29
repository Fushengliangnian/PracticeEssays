# from nameko.rpc import rpc, RpcProxy
# 
# 
# class Service:
#     name = "service"
# 
#     # we depend on the RPC interface of "another_service"
#     other_rpc = RpcProxy("another_service")
# 
#     @rpc  # `method` is exposed over RPC
#     def method(self):
#         # application logic goes here
#         pass
# 
# 
# # worker = Service()
# # worker.other_rpc = worker.other_rpc.get_dependency()
# # worker.method()
# # del worker
from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
