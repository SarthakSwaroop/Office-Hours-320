from collections import Counter
import random
    
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
    
    return sorted_common_times[:5]

# test data
availability = []
rankings = []
for i in range(20):
    # 6 random available times for each student in a week
    available_times = random.sample(range(1, 25), 6)
    availability.append(available_times)
    
    # top 3 ranked times for each student
    ranked_times = random.sample(available_times, 3)
    rankings.append(ranked_times)

def map_times_to_week(availability):
    # create a dictionary to map each available time to a day/time in the week
    time_map = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = [ '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM']
    for i, time in enumerate(sorted(set([item for sublist in availability for item in sublist]))):
        day = days[i % 7]
        time_map[time] = f"{day} {times[(time-1)%12]}"
    return time_map

# test function
n = 5
m = 5
common_times = find_common_times(availability, rankings, n, m)
time_map = map_times_to_week(availability)
print("Availability:")
for i, student_time in enumerate(availability):
    print(f"Student {i+1}:")
    for time in student_time:
        print(f"\t{time_map[time]}")
print("Rankings:")
for i, student_rankings in enumerate(rankings):
    print(f"Student {i+1}:")
    for j, time in enumerate(student_rankings):
        print(f"\t{j+1}. {time_map[time]}")
print("Most Popular Times:")
for time in common_times:
    print(f"\t{time_map[time]}")
