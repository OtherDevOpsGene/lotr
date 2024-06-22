"""App that uses an API with a key."""

import json
import requests

session = requests.Session()
resp = session.get("https://the-one-api.dev/v2/book")

data = resp.text
parsed = json.loads(data)

print(parsed)
