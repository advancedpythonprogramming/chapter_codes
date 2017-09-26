# 37.py

import json


json_string = '{"name":"Mark","age":34,' \
              '"marital_status": "married", "score" : 90.5}'
data = json.loads(json_string,
                  object_hook=lambda dict_obj:
                  [tuple((i, j)) for i, j in dict_obj.items()])
print(data)
