# Write your solution here

def best_average_grade(students: dict) -> tuple:
    best_student = ""
    best_grade = 0
    for name in students:
        sum_of_grades = 0
        for course in students[name]:
            sum_of_grades += course[1]
        average_grade = sum_of_grades / len(students[name])
        if average_grade > best_grade:
            best_grade = average_grade
            best_student = name
    return best_grade, best_student

def most_courses_completed(students: dict) -> tuple:
    max_student = ""
    max_completed = 0
    for name in students:
        if len(students[name]) > max_completed:
            max_student = name
            max_completed = len(students[name])
    return max_completed, max_student

def summary(students: dict) -> None:
    print(f"students {len(students)}")
    max_completed, max_student = most_courses_completed(students)
    print(f"most courses completed {max_completed} {max_student}")
    best_grade, best_student = best_average_grade(students)
    print(f"best average grade {best_grade} {best_student}")

def add_course(students: dict, name: str, course: tuple) -> None:
    if course[1] > 0:
        if len(students[name]) == 0:
            students[name] = [course]
        else:
            course_found = False
            for programme in students[name]:
                if course[0] == programme[0]:
                    course_found = True
                    if course[1] > programme[1]:
                        students[name].remove(programme)
                        students[name].append(course)
            if not course_found:
                students[name].append(course)

def print_student(students: dict, name: str) -> None:
    if name not in students:
        print(f"{name}: no such person in the database")
    elif len(students[name]) == 0:
        print(f"{name}:")
        print(f" no completed courses")
    else:
        print(f"{name}:")
        print(f" {len(students[name])} completed courses:")
        sum_of_grades = 0
        for course in students[name]:
            sum_of_grades += course[1]
            print(f"  {course[0]} {course[1]}")
        print(f" average grade {sum_of_grades/len(students[name])}")

def add_student(students: dict, name: str) -> None:
    if name not in students:
        students[name] = []

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
