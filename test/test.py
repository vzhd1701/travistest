import requests
r = requests.get("https://icanhazip.com/")
print(r.content)
