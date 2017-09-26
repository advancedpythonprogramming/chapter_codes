# request_usage.py

import requests

r = requests.get('http://localhost:8080/api/pow',
                 params={'v1': '10', 'v2': '2'})

print(r.text)

r = requests.get('http://localhost:8080/api/add',
                 params={'v1': '10', 'v2': '2'})

print(r.text)
