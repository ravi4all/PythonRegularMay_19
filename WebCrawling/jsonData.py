import json
import urllib.request as url

data = json.load(url.urlopen("https://geoip-db.com/json"))
print(data)