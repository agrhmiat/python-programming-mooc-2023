# Write your solution here

def print_stars(grades: list, grade_no: int) -> str:
    stars = 0
    for grade in grades:
        if grade == grade_no:
            stars += 1
    return "*" * stars

def get_grades(exam_points: list, exercise_points: list) -> list:
    grades = []
    for i in range(len(exam_points)):
        if exam_points[i] >= 10:
            if exam_points[i]+exercise_points[i] <= 14:
                grade = 0
            elif exam_points[i]+exercise_points[i] <= 17:
                grade = 1
            elif exam_points[i]+exercise_points[i] <= 20:
                grade = 2
            elif exam_points[i]+exercise_points[i] <= 23:
                grade = 3
            elif exam_points[i]+exercise_points[i] <= 27:
                grade = 4
            elif exam_points[i]+exercise_points[i] <= 30:
                grade = 5
        else:
            grade = 0
        grades.append(grade)
    return grades

def get_pass_percentage(exam_points: list, exercise_points: list) -> float:
    passed = 0
    for i in range(len(exam_points)):
        if exam_points[i] >= 10:
            if exam_points[i]+exercise_points[i] > 14:
                passed += 1
    return (passed / len(exam_points)) * 100

def get_points_average(exam_points: list, exercise_points: list) -> float:
    total_points = []
    for i in range(len(exam_points)):
        total_points.append(exam_points[i]+exercise_points[i])
    return sum(total_points) / len(total_points)

def get_exercise_points(exercises_completed: list) -> list:
    exercise_points = []
    for exercises in exercises_completed:
        exercise_points.append(exercises//10)
    return exercise_points

def main() -> None:
    exam_points = []
    exercises_completed = []

    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        parts = user_input.split(" ")
        exam_points.append(int(parts[0]))
        exercises_completed.append(int(parts[1]))

    exercise_points = get_exercise_points(exercises_completed)

    print("Statistics:")
    print(f"Points average: {get_points_average(exam_points, exercise_points)}")
    print(f"Pass percentage: {get_pass_percentage(exam_points, exercise_points):.1f}")

    grades = get_grades(exam_points, exercise_points)

    print("Grade distribution:")
    grade_no = 5
    while grade_no >= 0:
        print(f"{grade_no}: {print_stars(grades, grade_no)}")
        grade_no -= 1

main()
