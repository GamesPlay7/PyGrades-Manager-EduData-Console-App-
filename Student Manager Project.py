import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(students):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

students = load_data()

def add_student(students):
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists")
    else:
        students[name] = []
        save_data(students)
        print("Student added")

def add_grade(students):
    name = input("Enter student name: ")
    try:
        grade = int(input("Enter grade: "))
        if name not in students:
            print("Student not found")
        else:
            students[name].append(grade)
            save_data(students)
            print("Grade added")
    except ValueError:
        print("Please enter a valid number for the grade")

def show_students(students):
    if not students:
        print("No students")
    else:
        for name, grades in students.items():
            print(f"{name}: {grades}")

def average_grade(students):
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found")
    else:
        grades = students[name]
        if not grades:
            print("No grades")
        else:
            avg = sum(grades) / len(grades)
            result = round(avg, 2)
            print(f"{name}: {result}")

while True:
    print("\n--- Menu ---")
    print("1. Add student")
    print("2. Add grade")
    print("3. Show students")
    print("4. Average grade")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting...")
        break
    elif choice == "1":
        add_student(students)
    elif choice == "2":
        add_grade(students)
    elif choice == "3":
        show_students(students)
    elif choice == "4":
        average_grade(students)
    else:
        print("Invalid choice")