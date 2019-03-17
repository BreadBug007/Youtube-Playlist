import Credentials

youtube = Credentials.run()

def add_playlist(youtube, title, description = None, privacyStatus = 'private'):
    body = dict(
            snippet = dict(
            title = title,
            description = None
            ), status = dict(
                privacyStatus = 'private'
            )
            )
            
    try:        
        playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body=body
        ).execute()
        
    except:
        print("CreatePlaylist Error")
        return None
    
    print('New playlist Name: %s' % title)
    print('New playlist ID: %s' % playlists_insert_response['id'])
    
    return playlists_insert_response['id']
    

def run(youtube, title, privacy):
    
    playlistID = []
    
    for index in range(len(title)):    
        playlistID = add_playlist(youtube, title[index], privacy)
    
    return playlistID


