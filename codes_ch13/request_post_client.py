# request_post_client.py

import requests
import json

# Data as a form
form = {'id': 1,
        'name': 'Guido',
        'last_name': 'Van Rossum'}

# Header declares content type
header = {'Content-Type': 'application/json'}

# Make the request
r = requests.post('http://localhost:8080/upload',
                  headers=header,
                  data=json.dumps(form))

# Status code, 200 is 'OK'
print(r.status_code)
print(r.text)
