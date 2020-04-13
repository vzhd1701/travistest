import requests
r = requests.get("https://ipinfo.io/ip")
print(r.content)
