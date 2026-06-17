
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

# marks_calculator



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://code.swecha.org/vamshi_22/marks_calculator.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://code.swecha.org/vamshi_22/marks_calculator/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers
## Security

### Secret Scanning
This project uses Gitleaks to detect accidentally committed secrets such as API keys, passwords, and tokens.

Run locally:

```bash
gitleaks detect --source .
```

### Dependency Audit
This project uses pip-audit to identify known vulnerabilities in Python dependencies.

Run locally:

```bash
pip-audit -r requirements.txt
## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3).

See the LICENSE file for details.
```