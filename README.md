# Project Template: `aws-python`
## Setup
```sh
// activate Pipenv shell
$ pipenv shell

// install pipenv dependencies
$ pipenv install && pipenv install --dev

// install npm dependencies
$ npm install

// expose aws profile credentials
$ export AWS_PROFILE=<PROFILE_NAME>

// copy `config/env.yml.example` to `config/env.yml`
// populate `config/env.yml` with project secrets

// install dynamodb-local
$ npm run ddb:install

// `create` or `download` project ssm secrets:
// 1. `create` a new file `./config/ssm.sls.json`
$ npm run ssm:update

// 2. `download` an existing secrets
$ npm run ssm:download

// validate setup
$ npm run validate:all

// start-up apigateway and dynamodb localhost
$ npm run api:start
```
