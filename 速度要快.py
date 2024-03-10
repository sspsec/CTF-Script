import requests
import base64

session = requests.Session()

response = session.get('http://114.67.246.176:19795/')

str = response.headers['flag']

res = base64.b64decode(str).decode()

s = base64.b64decode(res.split(':')[1])

data = {
    'margin': s
}

r = session.post('http://114.67.246.176:19795/', data=data)

print(r.text)
