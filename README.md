# Project Template: `aws-python`

[![codecov](https://codecov.io/gh/Gilbertly/sls-starter-py/branch/master/graph/badge.svg?token=t4AGVARkds)](https://codecov.io/gh/Gilbertly/sls-starter-py)

## Setup

First ensure that your local environment is configured correctly:

```sh
// expose aws profile credentials
$ export AWS_PROFILE=<PROFILE_NAME>
```

### Installing Dependencies

```sh
// install npm dependencies
$ npm install

// activate Pipenv shell
$ pipenv shell

// install pipenv dependencies
$ pipenv install && pipenv install --dev
```

### SSM Parameters: `download`

Downloads existing project secrets from AWS environment to local file:

```sh
// download existing secrets from an ssm path
$ npm run ssm:download
```

### SSM Parameters: `update`

Creates or updates project secrets onto an AWS environment:

```sh
// create a new secrets file, eg. `./config/ssm.dev.json`
$ touch ./config/ssm.dev.json

// create or update secrets from a file
$ npm run ssm:update
```

### Validate Project Setup

Validates your development environment:

```sh
$ npm run validate:all

// start apigateway + dynamodb localhost
$ npm run ddb:install
$ npm run api:start
```

> _NOTE_: Run the command npm run ddb:install initially, and not everytime
> you are starting apigateway + dynamodb locally.
