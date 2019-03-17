import Credentials
import FindVideo
import UpdatePlaylist


root_dir = 'E:/'
youtube = Credentials.run()

VideoID, VideoName = FindVideo.run(youtube, root_dir)

playlistID = 'PLxlpouAsaxbvPIu96hP1afeRr-pT2RZy7'

UpdatePlaylist.run(youtube, playlistID, VideoID, VideoName)
