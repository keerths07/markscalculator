<<<<<<< HEAD
from backend.student_manager import add_student, view_students
from backend.marks_manager import add_marks, view_marks

while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Marks")
    print("4. View Marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        class_name = input("Enter Class: ")
        add_student(student_id, name, class_name)

    elif choice == "2":
        print(view_students())

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        subject = input("Enter Subject: ")
        marks = input("Enter Marks: ")
        add_marks(student_id, subject, marks)

    elif choice == "4":
        print(view_marks())

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")
=======
import streamlit as st

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Management System")

st.write("""
Welcome to the Student Management System.

Use the sidebar to navigate:
- Home
- Add Student
- Enter Marks
- View Results
""")
>>>>>>> 8e59598809e59ec169d087b5ce3c371f4fc76b10
