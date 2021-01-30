import spotipy
from spotipy.oauth2 import *
import SpotAnal
from SpotAnal import *


# Testing ID and Secret
#SPOTIPY_CLIENT_ID = '3d2e1d32b52f4d4a9f6496c70ff46446'
#SPOTIPY_CLIENT_SECRET = '08c836bdd7174ef2961b67637f5f7d24'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

# Temporary username for testing
username = 'aegis_sc'
# Gets the playlists from the Spotify User
playlists = sp.user_playlists(username)

##Displays the Name of Each Playlist for the User
# for playlist in playlists['items']:
#     print(playlist['name'])
##
## Displays a specific artist's discography
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
# for album in albums:
#     print(album['name'])
##
##Displays the URI and the Name of Each Playlist for the User
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print(
#             "%4d %s %s" %
#             (i +
#              1 +
#              playlists['offset'],
#              playlist['uri'],
#              playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
##


# Displays the name of every song in every playlist
for playlist in playlists['items']:
    print(playlist['name'])
    Tracks = sp.playlist_tracks(playlist['id'])
    for Track in Tracks['items']: 
        print(Track['track']['name'])
    print('\n\n')
