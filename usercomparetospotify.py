from PlaylistAnalyzer import *
import math  

class UserComparisonTool():
    def __init__(self):
        self.Analyzer = Analyzer()
        compared_playlists = []
    #Function that Calculate Root Mean Square  
    def rmsValue(self, arr, n): 
        square = 0
        mean = 0.0
        root = 0.0
        #Calculate square 
        for i in range(0,n): 
            square += (arr[i]**2) 
        
        #Calculate Mean  
        mean = (square / (float)(n)) 
        
        #Calculate Root 
        root = math.sqrt(mean) 
        
        return root 

    # Function to sort the list of tuples by its second item 
    def Sort_Tuple(tup):      
        # getting length of list of tuples 
        lst = len(tup)  
        for i in range(0, lst):  
            for j in range(0, lst-i-1):  
                if (tup[j][1] > tup[j + 1][1]):  
                    temp = tup[j]  
                    tup[j]= tup[j + 1]  
                    tup[j + 1]= temp  
        return tup  
    
    #compares the users value to a single playlist. returns a series of deltas
    def compare_playlists(self, user_score, spotify_playlist):
        delta_danceability = float(spotify_playlist[0]) - user_score[0]
        delta_tempo = float(spotify_playlist[1]) - user_score[1]
        delta_acousticness = float(spotify_playlist[4]) - user_score[4]
        delta_speechiness = float(spotify_playlist[5]) - user_score[5]
        delta_valence = float(spotify_playlist[6]) - user_score[6]
        delta_energy = float(spotify_playlist[7]) - user_score[7]
        return self.rmsValue([delta_danceability,delta_tempo, delta_acousticness, delta_speechiness, delta_valence, delta_energy], 6)        

    def usercomparison(self, user_playlist_library, spotify_playlist_library):
        #average all of the users playlists together to a single set of scores
        aggregated_user_scores = self.Analyzer.generate_user_scores(user_playlist_library)
        compared_playlists = []
        #compare the value to the playlist in the spotify library
        for playlist in spotify_playlist_library:
            playlist_rms = self.compare_playlists(aggregated_user_scores, spotify_playlist_library[playlist])
            compared_playlists.append((playlist_rms, playlist))
        compared_playlists.sort() 
        return compared_playlists[0][1]