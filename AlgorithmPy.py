import spotipy
from spotipy.oauth2 import *

# export SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
# export SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'
#SpotifyClientCredentials("3d2e1d32b52f4d4a9f6496c70ff46446","08c836bdd7174ef2961b67637f5f7d24")
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

username = 'kinghaloiii'
playlists = sp.user_playlists(username)
#artists= sp.current_user_top_artists(username)

for playlist in playlists['items']:
    print(playlist['name'])
    Tracks = sp.playlist_tracks(playlist['id'])
    for Track in Tracks['items']: 
        print(Track['track']['name'])
    print('\n\n')




#while playlists:
#    for i, playlist in enumerate(playlists['items']):
#        print(
#            "%4d %s %s" %
#            (i +
#             1 +
#             playlists['offset'],
#             playlist['uri'],
#             playlist['name']))
#    if playlists['next']:
#        playlists = sp.next(playlists)
#    else:
#        playlists = None

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])