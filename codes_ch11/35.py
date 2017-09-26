# 35.py

import json


json_string = '{"name":"Mark","age":34,' \
              '"marital_status": "married", "score" : 90.5}'
print(json.loads(json_string))
