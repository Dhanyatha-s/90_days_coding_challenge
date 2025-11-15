"""
Task: Build a student grade management system
use: lists, dicts, sets, tuples
Functions: Add students, calculate average, find top performers
"""
subjects = ["Science", "AI/ML", "Robotics","Communication"]

max_marks = 400

students = []

marks = []

def add_student():
    name = input("Enter Name of Student: ")
    students.append(name)

    print("New Student Added")

def add_marks():

    student_name = students[-1]
    print(f"Enter marks for {student_name}")
    

    student_marks = {}
    total = 0

    for sub in subjects:
        m = int(input(f"Enter the marks for {sub}: "))
        student_marks[sub] = m
        total += m

    marks.append({
        "name": student_name,
        "marks":student_marks,
        "total":total
    })

    print("Marks Added")


def calculate_avg(student_name):
    for record in marks:
        if record["name"] == student_name:
            avg = record["total"] / len(subjects)
            print(f"Average marks od the Student {student_name} is: {avg}")
            return
        
    print("Student not found!") 

def top_performace():

    sorted_students = sorted(marks,  key=lambda x: x["total"], reverse=True)

    topper = sorted_students[0]

    print(f" Top Performer: {topper['name']} with {topper['total']} marks")

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Calculate Average")
    print("4. Top Performer")
    print("5. Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        add_student()
    elif choice == 2:
        add_marks()
    elif choice == 3:
        name = input("Enter the student name: ")
        calculate_avg(name)
    elif choice == 4:
        top_performace()
    elif choice == 5:
        break
    else:
        print("Invalid choice")


