import spotipy
from spotipy.oauth2 import *
from SpotAnal import *

class info(self):
    def __init__(self):
        # export SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
        # export SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'
        #SpotifyClientCredentials("3d2e1d32b52f4d4a9f6496c70ff46446","08c836bdd7174ef2961b67637f5f7d24")
        # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        self.aggregated_information = []
        self.song_Data_List = []
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
        self.username = 'kinghaloiii'
        self.playlist_library = sp.user_playlists(username)
        #artists= sp.current_user_top_artists(username)
        self.Analyzer()

    def run(self):
        self.print_playlist_information(playlist_library)
        #for every playlist that exists within the users library
        for playlist in playlist_library['items']:
            track_list = sp.playlist_tracks(playlist['id'])
            #Track is an individual song information in the playlist 
            for track in track_list['items']: 
                #Get the ID of the song 
                songID = track['track']['id']
                #gathers information and creates a List of Dictionaries to analyze
                song_Data_List.append(sp.audio_features(songID))
            #Analyzes information and creates a method for creating a data unit for it. 
            self.aggregated_information = Analyzer.analyze_playlist(song_Data_List, playlist['tracks']['total'])
            self.Database_Information = {playlist['name'] : aggregated_information}

    def print_playlist_information(self,playlist_library):
        for playlist in playlist_library['items']:
            #print the name of the playlist
            print(playlist['name'])
            #print the total number of tracks in that playlist
            print(playlist['tracks']['total'])
            #A list of infomarion about every single track in a playlist 
            track_list = sp.playlist_tracks(playlist['id'])
            #Track is an individual song information in the playlist 
            for track in track_list['items']: 
                #Name of the song 
                songID = track['track']['id']
                print(track['track']['name'] + ':')
                #All audio feautres printed out
                print(sp.audio_features(songID) )
                print('\n')
            print('\n\n')

