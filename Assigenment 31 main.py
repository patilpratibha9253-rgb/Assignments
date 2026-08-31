# main.py

from student_utils.marks import calculate_average, highest_mark
from student_utils.grades import calculate_grade


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)
    highest = highest_mark(marks)
    grade = calculate_grade(average)

    students.append((name, average, highest, grade))


# Display results
print("\n===== STUDENT RESULTS =====")

for student in students:
    name, average, highest, grade = student

    print("\nName:", name)
    print("Average Mark:", average)
    print("Highest Mark:", highest)
    print("Grade:", grade)
