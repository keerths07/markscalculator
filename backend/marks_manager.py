from .database import read_csv, write_csv


def add_marks():
    student = {
        "student_id": input("Enter Student ID: "),
        "name": input("Enter Name: "),
        "subject": input("Enter Subject: "),
        "marks": input("Enter Marks: "),
    }

    write_csv(student)
    print("✅ Marks added successfully!")


def view_marks():
    records = read_csv()

    if not records:
        print("⚠️ No records found.")
        return

    print("\n===== MARKS LIST =====")
    for i, r in enumerate(records, start=1):
        print(
            f"{i}. ID: {r['student_id']} | Name: {r['name']} | Subject: {r['subject']} | Marks: {r['marks']}"
        )
