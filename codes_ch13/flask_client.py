# flask_client.py

import requests

r = requests.get('http://localhost:8080')
print('/: {}'.format(r.text))

r = requests.get('http://localhost:8080/resources')
print('/resources: {}'.format(r.text))

r = requests.get('http://localhost:8080/resources/1')
print('/resources/id: {}'.format(r.text))
