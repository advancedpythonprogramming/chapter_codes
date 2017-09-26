# request_google_images.py

import requests

# This URL contains the web service address
# and the required parameters

# %20 represents a 'space'

url = ('https://ajax.googleapis.com' +
       '/ajax/services/search/images?' +
       'v=1.0&q=copa%20america%20chile&as_filetype=jpg')

response = requests.get(url)
print(response.json())
