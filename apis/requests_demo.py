import requests
url = "https://xkcd.com/2141/"
url_image = "https://imgs.xkcd.com/comics/ui_vs_ux.png"

res = requests.get(url)
print(res.status_code) ## Prints the status code 
print("##" * 30)
print(res.text) ## prints html content
print("##" * 30)
print(res.json) ## prints json content
if res.status_code == 200:
    res2 = requests.get(url_image)
    with open("comic_image.png", "wb") as f:
        print("downloading image")
        f.write(res2.content)
else:
    print(f"url {url_image} is unreachable")





