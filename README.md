# lotr

A python app that uses an API with a key.

** This branch no longer works since HCP Vault Secrets was turned off. **
 
## Branches

The different branches demonstrate different approaches to dealing with the
API key securely.

* `main`- No key or authentication needed.
* `pre-commit` - Hard-coded secret with `pre-commit` hook.
* `aws-secrets-manager` - Retrieves the API key from [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

## The One API to rule them all

The API used for the demonstrations is [The One API](https://the-one-api.dev/).
