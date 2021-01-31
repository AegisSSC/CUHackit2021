from getuserplaylists import *
from getspotifyplaylists import *
from FileHandler import * 
from usercomparetospotify import *
#s = spotify_featured_playlists()
#s.main_component()
#u = user_playlist()
#u.main_component()

# X = Read_from_File('output.txt')
# print(X)
# def generate__reccomended_playlist():
    # if not Read_from_File("output.txt"):
# s = spotify_featured_playlists()
# s.main_component()
#s = spotify_featured_playlists()
#s.main_component()
UserComparisonTool = UserComparisonTool()
Spotify_Playlist = Read_from_File("output.txt")
username = input("Enter your username: ")
user = user_playlist(username)
user.main_component()
recommendation = UserComparisonTool.usercomparison(user.Database_Information, Spotify_Playlist)
print('\n' + recommendation+ '\n\n')
