import json
import random
import requests

url = 'http://localhost:8000/predict/'

data = {'features': [0,1,3,3]}
data = json.dumps(data)
response = requests.post(url, data)

prediction = []
for record in data:
    payload = {'features': record}
    payload = json.dumps(payload)
    response = requests.post(url, data)
    prediction.append(response.json().get('prediction'))
    
print(prediction)