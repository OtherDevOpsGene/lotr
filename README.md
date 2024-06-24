# lotr

A python app that uses an API with a key.

## Branches

The different branches demonstrate different approaches to dealing with the
API key securely.

* `main`- No key or authentication needed.
* `pre-commit` - Hard-coded secret with `pre-commit` hook.
* `vault` - Retrieves the API key from [HCP Vault Secrets](https://hashicorp.com/products/vault).
* `aws-secrets-manager` - Retrieves the API key from [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

## The One API to rule them all

The API used for the demonstrations is [The One API](https://the-one-api.dev/).
