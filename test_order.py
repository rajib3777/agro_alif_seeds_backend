import urllib.request
import json

payload = {
    "name": "Test User",
    "phone": "01711111111",
    "address": "Dhaka",
    "items": [{"product": 53, "quantity": 2}]
}

req = urllib.request.Request(
    'http://localhost:8000/api/orders/',
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        print("Response:", response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Status:", e.code)
    print("Error details:", e.read().decode('utf-8'))
