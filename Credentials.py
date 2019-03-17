import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def run():
    
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    
    with open('-oauth2.json') as f:
        creds = json.load(f)
        
        creds = Credentials(
                token = creds['access_token'],
                refresh_token = creds['refresh_token'],
                token_uri = creds['token_uri'],
                client_id = creds['client_id'],
                client_secret = creds['client_secret']
                )
    
    return build(API_SERVICE_NAME, API_VERSION, credentials = creds)


