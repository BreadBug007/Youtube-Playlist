## Features
- Searches youtube for songs in local directory and creates a playlist while adding the respective song to that playlist.

## Dependencies
### Youtube Data API v3
- Create [Google Developers](https://developers.google.com/api-client-library/python/start/get_started) account using Authorized API access(OAuth 2.0).

### mutagen
Python [module](https://mutagen.readthedocs.io/en/latest/) used to handle audio metadata. 
```
pip install mutagen
```

## Usage
- Use Generate_Token.py and Credentials.py to get authorization credentials required to use Youtube Data API.
- Create Playlists using CreatePlaylist.py and use the obtained playlistID in Initiate.py.
- Run Initiate.py for the required directory to add the resulted videos into playlists.



