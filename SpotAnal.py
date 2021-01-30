from collections import Counter
import math
import statistics

class Analyzer():

    def __init__():

    #Takes in all of the metrics from the individual songs, comparing them together
    def analyze_playlist(playlist, length = 100):
        ag_danceability = self.calculate_median_danceability(playlist)
        ag_tempo = self.calculate_median_tempo(playlist)
        ag_key = self.calculate_mode_key(playlist)
        ag_mode = self.calculate_mode_mode(playlist)
        ag_acousticness = self.calculate_mean_acousticness(playlist, length)
        ag_speechiness = self.calculate_mean_speechiness(playlist,length)
        ag_valence = self.calculate_mean_valence(playlist, length)
        ag_energy = self.calculate_mean_energy(playlist,length)

    def calculate_median(sorted_list):
        halfway = len(sorted_list) // 2
        if(halfway %2):
            return sorted(sorted_list)[halfway]
        else:
            return (sum(sorted(sample)[halfway - 1: halfway + 1])/2)
    
    def calculate_mode(sorted_list):
        c = Counter(sorted_list)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    def calculate_mean(List, length):
        var = 2
        min_cluster_size = 5
        for i in List:
            totalsum += i
        mean = totalsum / length 
        std = self.calculate_std_dev(List)
        for i in List:
            if(i < (mean - (std*var):
                sbset.append(i)
            elif(i > (mean - (std * var))):
                superset.append(i)

        if(len(subset) >= min_cluster_size):
            sub_mean = self.calculate_mean(subset, len(subset))
                
        if(len(superset) >= min_cluster_size):
            super_mean = self.calculate_mean(superset, len(superset))
        
        return mean, sub_mean, super_mean

    def calculate_std_dev(List): 
        return statistics.pstdev(List)
    
    def calculate_median_danceability(playlist):
        for song in playlist:
            danceability_list = song[danceability]
        return self.calculate_median(danceability_list)

    def calculate_median_tempo(playlist):
        for song in playlist:
            tempo_list = song[tempo]
        return self.calculate_median(tempo_list)
        
    def calculate_mode_key(playlist):
        for song in playlist:
            key_list = song[key]
        return self.calculate_mode(key_list)
        
    def calculate_mode_mode(playlist):
        for song in playlist:
            mode_list = song[mode]
        return self.calculate_mode(mode_list)
        
    def calculate_mean_acousticness(playlist,length):
        for song in playlist:
            acousticness_list = song[acousticness]
        return self.calculate_mode(acoutsticness_list)

    def calculate_mean_speechiness(playlist,length):
        for song in playlist:
            speechiness_list = song[speechiness]
        return self.calculate_mean(speechiness_list, length)
        
    def calculate_mean_valence(playlist,length):
        for song in playlist:
            valence_list = song[valence]
        return self.calculate_mean(valence_list, length)

    def calculate_mean_energy(playlist,length):
        for song in playlist:
            energy_list = song[energy]
        return self.calculate_mean(energy_list, length)
