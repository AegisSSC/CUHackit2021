from getuserplaylists import *
from getspotifyplaylists import *
from FileHandler import * 
from usercomparetospotify import *
# Creates an instance of UserComparision tool 
UserComparisonTool = UserComparisonTool()
# Output.txt holds the information for all Spotify playlists 
Spotify_Playlist = Read_from_File("output.txt")
# Prompts User for there Spotify Username and then runs the comparision, Printing which one is the closest 
username = input("Enter your username: ")
user = user_playlist(username)
user.main_component()
recommendation = UserComparisonTool.usercomparison(user.Database_Information, Spotify_Playlist)
print('\n' + recommendation+ '\n\n')
