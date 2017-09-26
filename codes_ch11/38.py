# 38.py

import json


def funcion(dict_obj):
    collection = []
    for k in dict_obj:
        collection.extend([k, str(dict_obj[k])])
    return collection

json_string = '{"name":"Mark","age":34,' \
              '"marital_status": "married", "score" : 90.5}'
data = json.loads(json_string, object_hook=lambda dict_obj: funcion(dict_obj))
print(data)
