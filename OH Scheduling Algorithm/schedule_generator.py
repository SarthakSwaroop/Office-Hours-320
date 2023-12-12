from collections import Counter
import random
import pandas as pd
from flask import Flask, jsonify
app = Flask(__name__)


'''Function to find popular times for office hours'''   
def find_common_times(availability, rankings, n, ranking_weight=1):
    all_times = []
    for student_time in availability:
        all_times.extend(student_time)
    
    # hash the frequency of each time
    time_counts = Counter(all_times)
    
    # return the n most popular times 
    common_times = [time for time, count in time_counts.most_common(n)]
    
    # sort common_times by cumulative ranking
    common_times_rankings = {}
    for time in common_times:
        common_times_rankings[time] = time_counts[time]
        for student_rankings in rankings:
            if time in student_rankings:
                common_times_rankings[time] += ((3 - student_rankings.index(time))*ranking_weight)
    sorted_common_times = sorted(common_times, key=lambda x: common_times_rankings[x], reverse=True)
    
    return sorted_common_times[:n], time_counts # return the n most popular times with at least m students attending, and the frequency of all times as a Counter object

'''Helper function to process data in csv files to desired format'''
def map_times_to_array(df):
    column_names = df.columns.tolist()
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

# Modify the format of the csv file so that each cell is "column_name cell_value"
def modify_format(file_path):
    df = pd.read_csv(file_path)
    df = df.drop(df.columns[0], axis=1)
    for index, row in df.iterrows():
        for column in df.columns:
            new_value = f"{column} {row[column]}"
            df.at[index, column] = new_value
    return df

#Find the number of students attending at least one of the office hours in the input schedule
def percent_coverage(df1,schedule):
    num_students = 0
    for index, row in df1.iterrows():
        if any(element in row.values for element in schedule):
            num_students += 1
    return num_students/len(df1)*100

##############################################################################################################################

'''Function to compute most popular office hours times (with parameterized ranking weight)'''
# Call function to return n most common times, using data from df1 and df2
def most_pop(df1,df2,n,ranking_weight=1):
    map1, availability = map_times_to_array(df1)
    map2, rankings = map_times_to_array(df2)
    #print("Availabilities:",availability) 
    #print("Rankings:",rankings)
    # number of office hours to recommend
    common_times, time_counts = find_common_times(availability, rankings, n, ranking_weight)
    #print("Recommended Times (hashed)",common_times)

    # Run inverse of hash function to get the original time strings
    inverse_hash_times = {v: k for k, v in map1.items()}
    common_times_original = [inverse_hash_times[time] for time in common_times]

    #print("Recommended Times (time strings)",common_times_original)
    #print("Frequency of each time:",[time_counts[time] for time in common_times])
    #print("Suggested popular schedule")
    #print(common_times_original)
    return common_times_original


'''Function to compute most popular office hours times with timings spread out across the week'''
# Spread out times so that the office hour schedule is spread out across the week
def spread_out(df1,df2,n):
    common_times_original = most_pop(df1,df2,2*n)
    days = [i.split(" ") for i in common_times_original]
    filtered_days = [day for i, day in enumerate(days) if day[0] not in [d[0] for d in days[:i]]]
    joined_days = [' '.join(day) for day in filtered_days]
    #add top n - len(joined_days) top times from common_times_original which is not already in joined_days to the end of the schedule
    for time in common_times_original:
        if time not in joined_days:
            joined_days.append(time)
        if len(joined_days) == n:
            break
    #print("Suggested popular + uniformly spread out schedule")
    #print(joined_days[:n])
    return joined_days[:n]


'''Heuristic Function to compute office hours schedule which maximizes students attending at least one office hour (no ranking weight)'''
# try several combinations of n unique office hours by sampling several time and return the schedule with the most students attending at least one office hour
def find_best_schedule(df1,n):
    # make a list of all unique time slots
    all_times = df1.values.flatten().tolist()
    all_times = list(set(all_times))
    #print("All times length:",len(all_times))
    best_schedule = []
    best_percent_students = 0
    for i in range(1000):
        schedule = random.sample(all_times,n)
        percent_students = percent_coverage(df1,schedule)
        if percent_students > best_percent_students:
            best_schedule = schedule
            best_percent_students = percent_students
    return best_schedule


##############################################################################################################################

'''HOW TO RUN'''

print("SAMPLE INPUT")
# Read data into dataframe from csv file
df1 = modify_format("Student_Availability.csv") #modify file name if needed
df2 = pd.read_csv("Student_Rankings.csv") #modify file name if needed
df2 = df2.drop(df2.columns[0], axis=1)
n = 5 # number of office hours to recommend
ranking_weight = 1 # weight to give to student rankings when computing most popular office hours times
print("Number of office hours to recommend:", n)
print("Ranking weight:", ranking_weight)

print("")
print("SAMPLE OUTPUT")
print("")

# The following code generates 3 different office hour schedules
# The first schedule generates the n most popular office hour times 
print("Most Popular Times:")
temp1 = most_pop(df1,df2,n,ranking_weight)
print(temp1)
print("Percentage of students covered:", round(percent_coverage(df1,temp1), 2))
print("")


# The second schedule generates the n most popular office hour times which are spread out across the week
print("Most Popular Times spread out across the Week:")
temp2 = spread_out(df1,df2,n)
print(temp2)
print("Percentage of students covered:", round(percent_coverage(df1,temp2), 2))
print("")

# The third schedule generates the office hour schedule which maximizes students attending at least one office hour (no ranking weight)
print("Most Popular Times with Most Students Covered:")
temp3 = find_best_schedule(df1, n)
print(temp3)
print("Percentage of students covered:", round(percent_coverage(df1, temp3), 2))

'''API endpoints'''

@app.route('/most_popular_times')
def get_most_popular_times(df1, df2, n, ranking_weight=1):
    temp1 = most_pop(df1, df2, n, ranking_weight)
    return jsonify(temp1,round(percent_coverage(df1,temp1), 2))

@app.route('/spread_out_times')
def get_spread_out_times(df1, df2, n):
    temp2 = spread_out(df1, df2, n)
    return jsonify(temp2,round(percent_coverage(df1,temp2), 2))

@app.route('/best_schedule')
def get_best_schedule(df1, n):
    temp3 = find_best_schedule(df1, n)
    return jsonify(temp3,round(percent_coverage(df1,temp3), 2))

if __name__ == '__main__':
    # Read data into dataframe from csv file
    df1 = modify_format("Student_Availability.csv") #modify file name if needed
    df2 = pd.read_csv("Student_Rankings.csv") #modify file name if needed
    df2 = df2.drop(df2.columns[0], axis=1)
    app.run()
