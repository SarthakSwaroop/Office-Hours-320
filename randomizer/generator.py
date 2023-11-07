import json
import random

def random_time():
    hours = random.randint(8, 18)
    minutes = random.randint(0, 5) * 10
    start_time = f'{hours:02d}:{minutes:02d}'
    end_time = f'{hours+1:02d}:{minutes:02d}'
    return f'{start_time}-{end_time}'

def generate_professor():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    professor = {"Professor": {day: random_time() if random.random() < 0.7 else None for day in days}}
    return professor

def generate_students(num_students, professor):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    students = []
    ids = set()
    for i in range(num_students):
        id = random.randint(10000000, 99999999)
        while id in ids:
            id = random.randint(10000000, 99999999)
        ids.add(id)
        availability = {}
        schedule = {}
        for day in days:
            availability[day], schedule[day] = random_time(), random_time()
            while availability[day] == schedule[day]:
                availability[day], schedule[day] = random_time(), random_time()
        rankings = sorted(days, key=lambda day: abs(int(professor["Professor"][day][0][:2]) - int(availability[day][0][:2])) if professor["Professor"][day] and availability[day] else float('inf'))
        students.append({
            "Student ID": id, 
            "availability": availability,
            "schedule": schedule,
            "rankings": rankings[:3]
        })
    return students

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

num_students = int(input("Enter the number of students: "))
professor = generate_professor()
students = generate_students(num_students, professor)
data = {"Professor": professor, "Students": students}
save_to_json(data, 'schedule.json')
print(f"Data saved to schedule.json")
