import spotipy
from spotipy.oauth2 import *

# export SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
# export SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'
#SpotifyClientCredentials("3d2e1d32b52f4d4a9f6496c70ff46446","08c836bdd7174ef2961b67637f5f7d24")
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

username = 'spotify'
playlists = sp.user_playlists(username) 
playlists2 = sp.user_playlists(username,offset=50)
#artists= sp.current_user_top_artists(username)
i = 0
for playlist,p2 in zip(playlists['items'],playlists2['items']):
    print(playlist['name'])
    print(p2['name'])
    i+=2
print(i)
    #print(playlist['tracks']['total'])
    #A list of infomarion about every single track in a playlist 
    # Tracks = sp.playlist_tracks(playlist['id'])
    # #Track is an individual song information in the playlist 
    # for Track in Tracks['items']: 
    #     #Name of the song 
    #     TrackID = Track['track']['id']
    #     print(Track['track']['name'] + ': ')
    #     #All audio feautres 
    #     print(sp.audio_features(TrackID) )
    #     print('\n')
    # print('\n\n')


### GETTING SPOTIFY USER FEAUTRED PLAYLIST AND DOING STUFF TO EM #### 
# SpotifyPL = sp.featured_playlists(limit = 30)
# for ting in SpotifyPL['playlists']['items']:
#     print(ting['name'])

