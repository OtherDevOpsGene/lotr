"""App that uses an API with a key"""

import json
import os
import requests

CHARACTER = "Isildur"
SECRET_URL = (
    "https://api.cloud.hashicorp.com/secrets/2023-06-13"
    + "/organizations/b4247403-70a5-4000-975c-3d49e6179bf7"
    + "/projects/d58eb77c-8afe-492f-bf2e-6538157be6be"
    + "/apps/lotr/open"
)


def get_vault_token():
    """Retrieves a short-lived Access Token to
    call HCP Vault Secrets. Uses environment credentials."""
    hcp_client_id = os.environ["HCP_CLIENT_ID"]
    hcp_client_secret = os.environ["HCP_CLIENT_SECRET"]

    token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    token_params = {
        "client_id": hcp_client_id,
        "client_secret": hcp_client_secret,
        "grant_type": "client_credentials",
        "audience": "https://api.hashicorp.cloud",
    }
    token_resp = requests.post(
        "https://auth.idp.hashicorp.com/oauth2/token",
        headers=token_headers,
        data=token_params,
    )
    token_data = token_resp.text
    token_json = json.loads(token_data)
    return {
        "Authorization": token_json["token_type"] + " " + token_json["access_token"]
    }


def get_secrets():
    """Returns all the secrets for the specified app as a dictionary."""
    token_headers = get_vault_token()
    vault_resp = requests.get(SECRET_URL, headers=token_headers)
    vault_data = vault_resp.text
    vault_json = json.loads(vault_data)

    vault_secrets = {}
    for secret in vault_json["secrets"]:
        name = secret["name"]
        value = secret["version"]["value"]
        vault_secrets[name] = value
    return vault_secrets


secrets = get_secrets()

headers = {"Authorization": "Bearer " + secrets["APIKEY"]}
resp = requests.get(
    "https://the-one-api.dev/v2/character?name=" + CHARACTER, headers=headers
)

data = resp.text
parsed = json.loads(data)

print(parsed)
