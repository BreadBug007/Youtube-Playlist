import YoutubeAPI
import sys


def playlist_items_insert(youtube, VideoName, properties,**kwargs):
    
    resource = YoutubeAPI.build_resource(properties)
    kwargs = YoutubeAPI.remove_empty_kwargs(**kwargs)
    
    try: youtube.playlistItems().insert(body=resource,**kwargs).execute()
    except:
        print('UpdatePlaylist Error')
        sys.exit()
    print('Done: ', VideoName)
    
    
def run(youtube, playlistID, VideoID, VideoName):
    
    for index in range(len(VideoID)):
        
        playlist_items_insert(youtube, VideoName[index],
            {'snippet.playlistId': playlistID,
             'snippet.resourceId.kind': 'youtube#video',
             'snippet.resourceId.videoId': VideoID[index],
             'snippet.position': ''},
              part='snippet')