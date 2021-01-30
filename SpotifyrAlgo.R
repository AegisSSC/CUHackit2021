library('spotifyr')

Sys.setenv(SPOTIFY_CLIENT_IT = "3d2e1d32b52f4d4a9f6496c70ff46446" )
Sys.setenv(SPOTIFY_CLIENT_SECRET = "08c836bdd7174ef2961b67637f5f7d24" )

access_token = get_spotify_access_token()
