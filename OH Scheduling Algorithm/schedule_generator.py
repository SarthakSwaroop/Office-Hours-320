from collections import Counter
import random
import pandas as pd

'''Function to find popular times for office hours'''   
def find_common_times(availability, rankings, n, m, ranking_weight=1):
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

'''Input data'''
# Read data into dataframe from csv file
df1 = modify_format("Student_Availability.csv")
df2 = pd.read_csv("Student_Rankings.csv")
df2 = df2.drop(df2.columns[0], axis=1)

'''Function to compute most popular office hours times (with parameterized ranking weight)'''
# Call function to return n most common times with at least m students attending, using data from df1 and df2
map1, availability = map_times_to_array(df1)
map2, rankings = map_times_to_array(df2)
#print("Availabilities:",availability) 
#print("Rankings:",rankings)
n = 12
m = 4
common_times, time_counts = find_common_times(availability, rankings, n, m, ranking_weight=1)
print("Recommended Times (hashed)",common_times)

# Run inverse of hash function to get the original time strings
inverse_hash_times = {v: k for k, v in map1.items()}
common_times_original = [inverse_hash_times[time] for time in common_times]

print("Recommended Times (time strings)",common_times_original)
print("Frequency of each time:",[time_counts[time] for time in common_times])
print("Suggested popular schedule")
print(common_times_original[:n//3])

'''Function to compute most popular office hours times with timings spread out across the week'''
# Spread out times so that the office hour schedule is spread out across the week
days = [i.split(" ") for i in common_times_original]
filtered_days = [day for i, day in enumerate(days) if day[0] not in [d[0] for d in days[:i]]]
joined_days = [' '.join(day) for day in filtered_days]
print("Suggested popular + uniformly spread out schedule")
print(joined_days[:n//3])

'''Function to compute office hours schedule which maximizes students attending at least one office hour (no ranking weight)'''
all_times = []
for student_time in availability:
    all_times.extend(student_time)

# read from csv file and make a list of all unique time slots
df = pd.read_csv("Student_Availability.csv")
df = df.drop(df.columns[0], axis=1)
column_names = df.columns.tolist()
for index, row in df.iterrows():
    for column in df.columns:
        new_value = f"{column} {row[column]}"
        df.at[index, column] = new_value
all_times = df.values.flatten().tolist()
all_times = list(set(all_times))
print("All times:",len(all_times))

# Read availability from CSV file
availability_df = pd.read_csv("Student_Availability.csv")
availability_df = availability_df.drop(availability_df.columns[0], axis=1)
# for each element x in column c, modify x to be "c x"
for column in availability_df.columns:
    for index, row in availability_df.iterrows():
        new_value = f"{column} {row[column]}"
        availability_df.at[index, column] = new_value
print("Availibility:", availability_df)

#Find the number of students attending at least one of the office hours in the input schedule
def percent_coverage(availability_df,schedule):
    num_students = 0
    for index, row in availability_df.iterrows():
        if any(element in row.values for element in schedule):
            num_students += 1
    return num_students/len(availability_df)*100

# try all possible combinations of n unique office hours by sampling several time and return the schedule with the most students attending at least one office hour
def find_best_schedule(availability_df,all_times,n):
    best_schedule = []
    best_num_students = 0
    for i in range(100):
        schedule = random.sample(all_times,n)
        num_students = percent_coverage(availability_df,schedule)
        if num_students > best_num_students:
            best_schedule = schedule
            best_num_students = num_students
    return best_schedule, best_num_students

print(find_best_schedule(availability_df,all_times,n//3))

'''HOW TO RUN'''

print("")
print("SAMPLE OUTPUT")
print("")

# The following code generates 3 different office hour schedules
# The first schedule generates the most popular office hour times with at least 4 students attending
print("Most Popular Times:")
print(common_times_original[:n//3])
print("Percentage of students covered:", round(percent_coverage(availability_df, common_times_original[:n//3]), 2))
print("")


# The second schedule generates the most popular office hour times with at least 4 students attending, and spread out across the week
print("Most Popular Times spread out across the Week:")
print(joined_days[:n//3])
print("Percentage of students covered:", round(percent_coverage(availability_df, joined_days[:n//3]), 2))
print("")

# The third schedule generates the office hour schedule which maximizes students attending at least one office hour (no ranking weight)
print("Most Popular Times with Most Students Covered:")
print(find_best_schedule(availability_df, all_times, n//3)[0])
print("Percentage of students covered:", round(percent_coverage(availability_df, find_best_schedule(availability_df, all_times, n//3)[0]), 2))
