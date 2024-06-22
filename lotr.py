"""App that uses an API with a key"""

import json
import boto3
import requests

CHARACTER = "Isildur"


def get_secret():
    """Retrieve the secret value from AWS Secrets Manager"""
    secret_name = "lotr/APIKEY"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    secret = get_secret_value_response["SecretString"]
    secret_json = json.loads(secret)
    return secret_json["APIKEY"]


APIKEY = get_secret()

headers = {"Authorization": "Bearer " + APIKEY}
resp = requests.get(
    "https://the-one-api.dev/v2/character?name=" + CHARACTER, headers=headers
)

data = resp.text
parsed = json.loads(data)

print(parsed)
