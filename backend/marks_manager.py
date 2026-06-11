from backend.database import write_csv, read_csv

def add_marks(student_id, subject, marks):
    write_csv("marks.csv", [student_id, subject, marks])

def view_marks():
    return read_csv("marks.csv")