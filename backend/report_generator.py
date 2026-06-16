from backend.marks_calculator import calculate_average, calculate_total



def generate_report(name, marks):
    total = calculate_total(marks)
    avg = calculate_average(marks)

    report = f"""
    Student Name: {name}
    Total Marks: {total}
    Average: {avg}
    """
    return report
