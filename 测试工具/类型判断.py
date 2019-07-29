# print(0 <= len({}) <= 1000000)
#
# a = b = []
#
# a.append(1)
# print(b)
#
# a = ""
# # print(type(a))
# # assert isinstance(a, str)
# # print(11)

# a = [1,2]
# b = [3,4]
# a = a + b
# print(a)

# code_list = [{
#     'user': 1,
#     'add': 2,
#     'ss': 6
#     },
#     {
#         'user': 3,
#         'add': 4,
#         'ss': 7
#
#     }
#
# ]
# user_ids = []
# add_ids = []
# ss_ids = []
# code_ids = [code.items() for code in code_list]
# for code in code_list:
#     user_ids.append(code.get('user'))
#     add_ids.append(code.get('add'))
#     ss_ids.append(code.get('ss'))
#

# {"user": {"$in": user_ids}, "add": {"$in": add_ids}, "ss": {"$in": ss_ids}}
import json

ret = json.dumps({"show_type":2,"main_material_id":14038,"is_drop":True,"tmp_order":1})
print(repr(ret))
