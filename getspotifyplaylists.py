import spotipy
from spotipy.oauth2 import *
from PlaylistAnalyzer import *


### STUFF I ADDED TO PULL OTHER STUFF ### 

### GETTING SPOTIFY USER FEAUTRED PLAYLIST AND DOING STUFF TO EM #### 

class spotify_featured_playlists():
    def __init__(self):
        # export SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
        # export SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'
        #SpotifyClientCredentials("3d2e1d32b52f4d4a9f6496c70ff46446","08c836bdd7174ef2961b67637f5f7d24")
        self.aggregated_information = []
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
        self.username = 'spotify'
        playlists = self.sp.user_playlists(self.username)
        playlists2 =  self.sp.user_playlists(self.username,offset=50)
        playlists.update(playlists2)
        self.playlist_library = playlists
        #artists= sp.current_user_top_artists(username)
        self. Analyzer = Analyzer()

    def main_component(self):
        self.print_playlist_information(self.playlist_library)
        #for every playlist that exists within the users library
        for playlist in self.playlist_library['items']:
            song_Data_List = []
            track_list = self.sp.playlist_tracks(playlist['id'])
            #Track is an individual song information in the playlist 
            for track in track_list['items']: 
                #Get the ID of the song 
                songID = track['track']['id']
                #gathers information and creates a List of Dictionaries to analyze
                song_Data_List.append(self.sp.audio_features(songID))
            #Analyzes information and creates a method for creating a data unit for it. 
            self.aggregated_information = self.Analyzer.analyze_playlist(song_Data_List, playlist['tracks']['total'])
            self.Database_Information = {playlist['name'] : self.aggregated_information}
            print("Playlist Name: "+ playlist['name'] + " Playlist data: ")
            print(self.Database_Information[playlist['name']])
        # self.Write_to_file(self.Database_Information,"output.txt")

    def print_playlist_information(self,playlist_library):
        for playlist in self.playlist_library['items']:
            #print the name of the playlist
            print(playlist['name'])
            #print the total number of tracks in that playlist
            print(playlist['tracks']['total'])
            #A list of infomarion about every single track in a playlist 
            track_list = self.sp.playlist_tracks(playlist['id'])
            #Track is an individual song information in the playlist 
            for track in track_list['items']: 
                #Name of the song 
                songID = track['track']['id']
                print(track['track']['name'] + ':')
                #All audio feautres printed out
                print(self.sp.audio_features(songID) )
                print('\n')
            print('\n\n')

            
    def Write_to_file(self,Database_Information,output):
        f = open(output,"a")
        for item in Database_Information.items():
            f.write(str(item) + '\n')
        f.close()

            # #A list of infomarion about every single track in a playlist 
            # track_list = self.sp.playlist_tracks(playlist['id'])
            # #Track is an individual song information in the playlist 
            # for track in track_list['items']: 
            #     #Name of the song 
            #     songID = track['track']['id']
            #     print(track['track']['name'] + ':')
            #     #All audio feautres printed out
            #     print(self.sp.audio_features(songID) )
            #     print('\n')
            # print('\n\n')
