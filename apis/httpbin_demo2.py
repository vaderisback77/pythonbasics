import requests
from pprint import pprint

payload = {"name": "Saurabh", "Age": 39}
url = "https://httpbin.org/post"
res = requests.post(url, data=payload)
print(res.text)
print(res.json())

url2 = "https://httpbin.org/basic-auth/saurabh/saran123"
res2 = requests.get(url2, auth=("saurabh", "saran123"))
print(res2.status_code, "\n", res2.text)
