# request_response_client.py

import requests

r = requests.get('http://localhost:8080/api')
print('{}'.format(r.json()))

r = requests.get('http://localhost:8080/api')
print('{}'.format(r.json()))
