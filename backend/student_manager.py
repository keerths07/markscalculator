import csv

FILE = "data/students.csv"

def add_student(student_id, name, class_name):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name, class_name])

def view_students():
    with open(FILE, "r") as f:
        return f.readlines()