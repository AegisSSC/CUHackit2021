from getuserplaylists import *
from getspotifyplaylists import *
from FileHandler import * 
from usercomparetospotify import *

# def generate__reccomended_playlist():
    # if not Read_from_File("output.txt"):
    #     s = spotify_featured_playlists()
    #     s.main_component()
UserComparisonTool = UserComparisonTool()
Spotify_Playlist = Read_from_File("output.txt")
user = user_playlist()
user.main_component()
recommendation = UserComparisonTool.usercomparison(user.Database_Information, Spotify_Playlist)
print(recommendation)