import json
import urllib.request
import urllib.parse

url ="https://statsapi.web.nhl.com/api/v1/teams"
response = urllib.request.urlopen(url)
raw = response.read()
data = json.loads(raw)

def get_team_name(city):
    for item in data["teams"]:
        if item['venue']['city'] == city:
            return data["teams"][0]['name']

print(get_team_name("Newark"))
