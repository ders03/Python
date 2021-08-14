import json
import urllib.request
import urllib.parse

url = " https://www.balldontlie.io/api/v1/players"
response = urllib.request.urlopen(url)
raw = response.read()
data = json.loads(raw)


print(data["data"][1])
