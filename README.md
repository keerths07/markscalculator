📌 Project Overview

This is a Python-based Student Feedback and Marks Management System.
It helps manage student details, store marks, and generate performance reports using simple CSV files as a lightweight database.

⚙️ Features
Add new student details
Store and manage student marks
Calculate total marks
Calculate average marks
Generate student performance reports
Simple file-based data storage (CSV)
📁 Project Structure
student_feedback_system/
├── backend/
│   ├── __init__.py
│   ├── student_manager.py
│   ├── marks_manager.py
│   ├── report_generator.py
│   └── database.py
│
├── data/
│   ├── students.csv
│   ├── marks.csv
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Clone the repository
git clone <your-repo-link>
cd student_feedback_system
2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Run the application
python app.py
📊 Modules Description
📄 student_manager.py
Add student details
View student list
📄 marks_manager.py
Add marks for students
Retrieve marks data
📄 report_generator.py
Calculate total marks
Calculate average marks
Generate student report
📄 database.py
Handle CSV file read/write operations
📂 Data Files
students.csv

Stores student information like:

student_id, name, class
marks.csv

Stores marks information like:

student_id, subject, marks
🧠 Technologies Used
Python 🐍
CSV (File Handling)
🎯 Future Improvements
Add login system (Admin / Student)
Replace CSV with SQLite database
Build web version using Flask
Add graphical dashboard
👨‍💻 Author

Created by: Your Name

📌 License

This project is for educational purposes only.