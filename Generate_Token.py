import os
import sys

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

CLIENT_SECRETS_FILE = "client_secret_2.json"
SCOPE = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  scope=SCOPE)

storage = Storage("-oauth2.json")
credentials = storage.get()

if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)