from collections import Counter
import math
import statistics


class Analyzer():

    def __init__(self):
        self.var = 2
        self.min_cluster_size = 5
        self.danceability_list = []
        self.tempo_list = []
        self.key_list = []
        self.valence_list = []
        self.energy_list = []
        self.speechiness_list = []
        self.acousticness_list = []
        self.mode_list = []
        self.key_list = []
    
    #Function:          calculate_median
    #Description:       Calculates the median of a given data set
    #Preconditions:     sorted_list is a list of numbers that should be sorted
    #Postconditions:    Returns a 5 decimal floating type to the user as the median
    def calculate_median(self, sorted_list):
        halfway = len(sorted_list) // 2
        if(halfway %2):
            return round(sorted(sorted_list)[halfway],5)
        else:
            return round((sum(sorted(sorted_list)[halfway - 1: halfway + 1])/2),5)
    
    #Function:          calculate_mode
    #Description:       Calculates the mode of a given data set
    #Preconditions:     sorted_list is a list of numbers that should be sorted
    #Postconditions:    Returns a 5 decimal floating type to the user as the mode
    def calculate_mode(self, sorted_list):
        c = Counter(sorted_list)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    #Function:          calculate_mean
    #Description:       Calculates the mean of a given data set
    #Preconditions:     list is a list of numbers that should be sorted, length is the length of the List
    #Postconditions:    Returns a 5 decimal floating type to the user as the mean
    def calculate_mean(self, List, length):
        mean = statistics.mean(List)
        return round(mean,5)


    #Function:          calculate_std_dev
    #Description:       Calculates the standard deviation of a given data set
    #Preconditions:     list is a list of numbers
    #Postconditions:    Returns a 5 decimal floating type to the user as the standard deviation
    # def calculate_std_dev(self, List): 
    #     return round(statistics.pstdev(List),5)
    
    #Function:          calculate_median_danceability
    #Description:       determines the median danceability rating for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal floating type to the user as the median_danceability
    def calculate_median_danceability(self, playlist):
        for song in playlist:
            self.danceability_list.append(song[0]["danceability"])
        return self.calculate_median(self.danceability_list)

    #Function:          calculate_median_tempo
    #Description:       determines the median tempo rating for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal floating type to the user as the median_tempo
    def calculate_median_tempo(self, playlist):
        for song in playlist:
            self.tempo_list.append(song[0]["tempo"])
        return self.calculate_median(self.tempo_list)
    
    #Function:          calculate_mode_key
    #Description:       determines the most commonly used musical key for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns an int type to the user as the most common musical key 
    def calculate_mode_key(self, playlist):
        for song in playlist:
            self.key_list.append(song[0]["key"])
        return self.calculate_mode(self.key_list)
    
    #Function:          calculate_mode_mode
    #Description:       determines the most commonly used mode (major or minor key) for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a binary integer to the user as the most commonly used key signature
    def calculate_mode_mode(self, playlist):
        for song in playlist:
            self.mode_list.append(song[0]["mode"])
        return self.calculate_mode(self.mode_list)
        

    #Function:          calculate_mean_acousticness
    #Description:       determines the average acousticness for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal float type to the user as the average acousticness
    def calculate_mean_acousticness(self, playlist,length):
        for song in playlist:
            self.acousticness_list.append(song[0]["acousticness"])
        return self.calculate_mean(self.acousticness_list, length)


    #Function:          calculate_mean_speechiness
    #Description:       determines the average acousticness for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal float type to the user as the average speechiness
    def calculate_mean_speechiness(self, playlist,length):
        for song in playlist:
            self.speechiness_list.append(song[0]["speechiness"])
        return self.calculate_mean(self.speechiness_list, length)
        
    #Function:          calculate_mean_valence
    #Description:       determines the average valence for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal float type to the user as the average valence
    def calculate_mean_valence(self, playlist,length):
        for song in playlist:
            self.valence_list.append(song[0]["valence"])
        return self.calculate_mean(self.valence_list, length)


    #Function:          calculate_mean_energy
    #Description:       determines the average energy for the whole playlist. 
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #Postconditions:    Returns a 5 decimal float type to the user as the average energy
    def calculate_mean_energy(self, playlist,length):
        for song in playlist:
            self.energy_list.append(song[0]["energy"])
        return self.calculate_mean(self.energy_list, length)

    #Function:          analyze_playlist
    #Description:       #Takes in all of the metrics from the individual songs, comparing them together
    #Preconditions:     playlist is a list of maps that correspond to songs and their information as delivered by spotify
    #                   length is the total length of the playlist that defaults to 100
    #Postconditions:    Returns an array to the user to represent the average for the playlist
    def analyze_playlist(self, playlist, length = 100):
        ag_danceability = self.calculate_median_danceability(playlist)
        ag_tempo = self.calculate_median_tempo(playlist)
        ag_key = self.calculate_mode_key(playlist)
        ag_mode = self.calculate_mode_mode(playlist)
        ag_acousticness = self.calculate_mean_acousticness(playlist, length)
        ag_speechiness = self.calculate_mean_speechiness(playlist,length)
        ag_valence = self.calculate_mean_valence(playlist, length)
        ag_energy = self.calculate_mean_energy(playlist,length)
        return [ag_danceability, ag_tempo, ag_key, ag_mode, ag_acousticness, ag_speechiness, ag_valence, ag_energy]