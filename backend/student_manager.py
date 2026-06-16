import csv

FILE = "data/students.csv"


def add_student(student_id, name, class_name):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name, class_name])


def view_students():
    with open(FILE, "r", encoding="utf-8") as f:
        return f.readlines()
