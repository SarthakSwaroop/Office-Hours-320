from collections import Counter
import random
import pandas as pd
    
def find_common_times(availability, rankings, n, m):
    all_times = []
    for student_time in availability:
        all_times.extend(student_time)
    
    # hash the frequency of each time
    time_counts = Counter(all_times)
    
    # return the n most popular times with at least m students attending
    common_times = [time for time, count in time_counts.most_common(n) if count >= m]
    
    # sort common_times by cumulative ranking
    common_times_rankings = {}
    for time in common_times:
        common_times_rankings[time] = 0
        for student_rankings in rankings:
            if time in student_rankings:
                common_times_rankings[time] += (3 - student_rankings.index(time))
    sorted_common_times = sorted(common_times, key=lambda x: common_times_rankings[x], reverse=True)
    
    return sorted_common_times[:n]

def map_times_to_array(file_path,bool):
    df = pd.read_csv(file_path)
    df = df.drop(df.columns[0], axis=1)
    column_names = df.columns.tolist()
    if bool:
        for index, row in df.iterrows():
            for column in df.columns:
                new_value = f"{column} {row[column]}"
                df.at[index, column] = new_value

    print(df)

    # Create a dictionary to hash each element to a unique integer
    element_map = {}
    for column in column_names:
        for cell in df[column]:
            if cell not in element_map:
                element_map[cell] = hash(cell)

    # Create an array of arrays with each subarray representing a row of the new hashed availibility list
    new_avlist = []
    for i in range(len(df)):
        row_array = []
        for column in column_names:
            cell = df[column][i]
            row_array.append(element_map[cell])
        new_avlist.append(row_array)

    return element_map, new_avlist


# test function to return n most common times with at least m students attending, inputing data from csv files
map1, availability = map_times_to_array("Student_Availability.csv",True)
map2, rankings = map_times_to_array("Student_Rankings.csv",False)
#print(availability)
#print(rankings)

n = 2
m = 1
common_times = find_common_times(availability, rankings, n, m)

# Run inverse of hash function to get the original time strings
inverse_hash_times = {v: k for k, v in map1.items()}
common_times_original = [inverse_hash_times[time] for time in common_times]

print(common_times_original)
