from getuserplaylists import *
from getspotifyplaylists import *
from FileHandler import * 
from usercomparetospotify import *
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        user_token = request.get_json()
        return 'OK', 200


#s = spotify_featured_playlists()
#s.main_component()
#u = user_playlist()
#u.main_component()

X = Read_from_File('output.txt')
print(X)
# def generate__reccomended_playlist():
    # if not Read_from_File("output.txt"):
    #     s = spotify_featured_playlists()
    #     s.main_component()
# UserComparisonTool = UserComparisonTool()
# Spotify_Playlist = Read_from_File("output.txt")
# user = user_playlist()
# user.main_component()
# recommendation = UserComparisonTool.usercomparison(user.Database_Information, Spotify_Playlist)
# print(recommendation)
