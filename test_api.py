import urllib.request
import json
try:
    req = urllib.request.urlopen('http://localhost:8000/api/products/')
    res = json.loads(req.read())
    print(json.dumps(res[:2], indent=2))
except Exception as e:
    print("Error:", e)
