"""App that uses an API with a key."""

import json
import requests

APIKEY = 'secret'
CHARACTER = 'Isildur'

session = requests.Session()
session.headers.update({'Authorization': 'Bearer '+ APIKEY})
resp = session.get("https://the-one-api.dev/v2/character?name=" + CHARACTER)

data = resp.text
parsed = json.loads(data)

print(parsed)
