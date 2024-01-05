# Write your solution here

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = 0
        sum_of_exercises = 0
        for exercise in parts[1:]:
            sum_of_exercises += int(exercise)
        exercises[parts[0]] = sum_of_exercises

exams = {}

with open(exam_points) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = 0
        sum_of_exam_pts = 0
        for points in parts[1:]:
            sum_of_exam_pts += int(points)
        exams[parts[0]] = sum_of_exam_pts

grades = {}

for id, student in students.items():
    total_points = exams[id] + int(exercises[id]/40*10)
    if total_points < 15:
        grade = 0
    elif total_points < 18:
        grade = 1
    elif total_points < 21:
        grade = 2
    elif total_points < 24:
        grade = 3
    elif total_points < 28:
        grade = 4
    else:
        grade = 5
    grades[id] = grade

print(f"name{" ":26}exec_nbr{" ":2}exec_pts.{" ":1}exm_pts.{" ":2}tot_pts.{" ":2}grade{" ":5}")
for id, student in students.items():
    print(f"{student:<30}{exercises[id]:<10}{int(exercises[id]/40*10):<10}{exams[id]:<10}{exams[id]+int(exercises[id]/40*10):<10}{grades[id]:<10}")
