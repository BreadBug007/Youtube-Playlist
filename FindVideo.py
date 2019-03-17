import os
import mutagen
import YoutubeAPI

def get_song_info(root, search):
    
    location = root + '\\' + search
    
    song = mutagen.File(location, options = None)
    
    
    try:
        if search.endswith(".mp3"):
            return song['TPE1'][0] + ' ' + song['TIT2'][0]
        else:
            return song['artist'][0] + ' ' + song['title'][0]
    except:
        return search



def run(youtube):
    
    root_dir = r'E:/'
    
    file_dict = {}
    
    filters = ('.mp3', '.flac')
    
    for root, dirs, files in os.walk(root_dir):
        temp = []
        for file in files:        
            if file.endswith(filters):
                temp.append(file)
        file_dict[root] = temp

    VideoId, VideoName = [], []  
    
    for root in file_dict.keys():
        for search in file_dict[root]:
            location = root + '\\' + search
            size = os.path.getsize(location)
            if size > 0:
                search = get_song_info(root, search)
                search_list = youtube_search(youtube, search)
                if search_list == 'Error': 
                    return VideoId, VideoName
                Id = search_list['items'][0]['id']['videoId']
                VideoId.append(Id)
                VideoName.append(search)
                print('Name:', search)
                print('Video: https://www.youtube.com/watch?v=' + Id)
    return VideoId, VideoName



def youtube_search(youtube, search):
    return keyword_search(youtube, part='snippet',
    maxResults=5,
    q=search,
    type='Video')
    
def keyword_search(youtube, **k):
    k = YoutubeAPI.remove_empty_kwargs(**k)
    try:
        return youtube.search().list(**k).execute()
    except:
        print('Video Not Found')
        return 'Error'
