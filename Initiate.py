import Credentials
import FindVideo
import UpdatePlaylist

youtube = Credentials.run()

VideoID, VideoName = FindVideo.run(youtube)

playlistID = 'Insert_Playlist_Id'

UpdatePlaylist.run(youtube, playlistID, VideoID, VideoName)
