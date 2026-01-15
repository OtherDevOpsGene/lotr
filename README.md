# lotr

A python app that uses an API with a key.

Accompanying slides are available at 
https://www.slideshare.net/slideshow/kcdc-keeping-secrets-out-of-your-pipeline/269947553.

**Note:** Cloud9 needs an `m5.large` instance, or it will run out of compute credits. A `t3.small` is not enough.

## Branches

The different branches demonstrate different approaches to dealing with the
API key securely.

* `main`- No key or authentication needed.
* `pre-commit` - Hard-coded secret with `pre-commit` hook.
* `aws-secrets-manager` - Retrieves the API key from [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

## The One API to rule them all

The API used for the demonstrations is [The One API](https://the-one-api.dev/).
