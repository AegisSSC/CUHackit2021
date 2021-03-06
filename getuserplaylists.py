import spotipy
from spotipy.oauth2 import *
from PlaylistAnalyzer import *

class user_playlist:
    def __init__(self, un = 'aegis_sc'):
        # export SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
        # export SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'
        #SpotifyClientCredentials("3d2e1d32b52f4d4a9f6496c70ff46446","08c836bdd7174ef2961b67637f5f7d24")
        # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        self.aggregated_information = []
        self.Database_Information = dict()
        self.song_Data_List = []
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
        self.username = un
        self.playlist_library = self.sp.user_playlists(self.username)
        self.Analyzer = Analyzer()

    def main_component(self):
        self.print_playlist_information(self.playlist_library)
        #for every playlist that exists within the users library
        for playlist in self.playlist_library['items']:
            track_list = self.sp.playlist_tracks(playlist['id'])
            #Track is an individual song information in the playlist 
            for track in track_list['items']: 
                #Get the ID of the song 
                songID = track['track']['id']
                #gathers information and creates a List of Dictionaries to analyze
                self.song_Data_List.append(self.sp.audio_features(songID))
            #Analyzes information and creates a method for creating a data unit for it. 
            self.aggregated_information = self.Analyzer.analyze_playlist(self.song_Data_List, playlist['tracks']['total'])
            self.Database_Information[playlist['name']] =  self.aggregated_information
            print("Playlist Name: "+ playlist['name'] + " Playlist data: ")
            print(self.Database_Information[playlist['name']])
        return
            

    def print_playlist_information(self,playlist_library):
        for playlist in playlist_library['items']:
            #print the name of the playlist
            print(playlist['name'])
            #print the total number of tracks in that playlist
            print(playlist['tracks']['total'])
