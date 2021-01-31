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
        
    def calculate_median(self, sorted_list):
        halfway = len(sorted_list) // 2
        if(halfway %2):
            return round(sorted(sorted_list)[halfway],5)
        else:
            return round((sum(sorted(sorted_list)[halfway - 1: halfway + 1])/2),5)
    
    def calculate_mode(self, sorted_list):
        c = Counter(sorted_list)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    def calculate_mean(self, List, length):
        mean = statistics.mean(List)
        return round(mean,5) #, sub_mean, super_mean

    # def calculate_std_dev(self, List): 
    #     return round(statistics.pstdev(List),5)
    
    def calculate_median_danceability(self, playlist):
        for song in playlist:
            self.danceability_list.append(song[0]["danceability"])
        return self.calculate_median(self.danceability_list)

    def calculate_median_tempo(self, playlist):
        for song in playlist:
            self.tempo_list.append(song[0]["tempo"])
        return self.calculate_median(self.tempo_list)
        
    def calculate_mode_key(self, playlist):
        for song in playlist:
            self.key_list.append(song[0]["key"])
        return self.calculate_mode(self.key_list)
        
    def calculate_mode_mode(self, playlist):
        for song in playlist:
            self.mode_list.append(song[0]["mode"])
        return self.calculate_mode(self.mode_list)
        
    def calculate_mean_acousticness(self, playlist,length):
        for song in playlist:
            self.acousticness_list.append(song[0]["acousticness"])
        return self.calculate_mode(self.acousticness_list)

    def calculate_mean_speechiness(self, playlist,length):
        for song in playlist:
            self.speechiness_list.append(song[0]["speechiness"])
        return self.calculate_mean(self.speechiness_list, length)
        
    def calculate_mean_valence(self, playlist,length):
        for song in playlist:
            self.valence_list.append(song[0]["valence"])
        return self.calculate_mean(self.valence_list, length)

    def calculate_mean_energy(self, playlist,length):
        for song in playlist:
            self.energy_list.append(song[0]["energy"])
        return self.calculate_mean(self.energy_list, length)

    #Takes in all of the metrics from the individual songs, comparing them together
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