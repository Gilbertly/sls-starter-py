import sentry_sdk
from os import environ
from sentry_sdk import capture_exception

sentry_sdk.init(dsn=environ.get('SENTRY_DSN'))


def handler(event, context):
  try:
    event_param = event['some_param']
  except Exception as error:
    capture_exception(error)

  return f"Event param: '{event_param}'"
