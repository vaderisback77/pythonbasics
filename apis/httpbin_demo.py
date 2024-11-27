import requests
url = "https://httpbin.org/get"

# additional parameters passing to the url as a dictionary
payload = {"page": 2, "count": 25}
res = requests.get(url, params=payload)
if res.ok:
    print("Website is reachable, yay!")
    print(res.headers)  ## printing headers
    print("####" * 20)  
    print(res.url)      ## printing the url with parameters
    print("####" * 20)
    print(res.text)     ## printing data
    





