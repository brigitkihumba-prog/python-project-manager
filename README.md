Python Project Management CLI Tool

Overview

The Python Project Management CLI Tool is a command-line application developed in Python 3. It allows users to manage users, projects, and tasks from a terminal. The application uses object-oriented programming, command-line arguments, and JSON file handling to organise and save project information.

Features

- User management: Add users and display the registered users.
- Project management: Create projects, associate them with users, and list projects.
- Task management: Add tasks to projects, assign tasks to users, and mark tasks as complete.
- Data persistence: Save and load users, projects, and tasks using a JSON file.
- Command-line interface: Use "argparse" subcommands to perform actions from the terminal.
- Formatted output: Use the Rich Python package to display information in readable tables.
- Error handling: Handle missing or invalid JSON data and provide useful feedback.

Technologies Used

- Python 3.10 or later
- "argparse" for command-line arguments
- "json" for data storage
- "Rich" for formatted terminal output
- "unittest" for automated testing
- Git and GitHub for version control

Project Structure

python-project-manager/
├── main.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   ├── __init__.py
│   └── storage.py
├── data/
│   └── projects.json
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── requirements.txt
├── .gitignore
└── README.md

Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Replace "YOUR_GITHUB_REPOSITORY_URL" with the HTTPS URL of this repository.

2. Navigate into the project directory

cd python-project-manager

3. Create a virtual environment

python3 -m venv .venv

4. Activate the virtual environment

On Ubuntu or Linux:

source .venv/bin/activate

5. Install the required dependency

python -m pip install -r requirements.txt

Usage

Run commands from the project directory with the virtual environment activated.

Display available commands

python main.py --help

Add a user

python main.py add-user --name "Jane Doe" --email "jane@example.com"

List users

python main.py list-users

Add a project

python main.py add-project --user "Jane Doe" --title "Website Project" --description "Create a website" --due-date "2026-12-31"

List projects

python main.py list-projects

To list projects associated with a particular user:

python main.py list-projects --user "Jane Doe"

Add a task

python main.py add-task --project "Website Project" --title "Create homepage" --assigned-to "Jane Doe"

Complete a task

python main.py complete-task --project "Website Project" --title "Create homepage"

Object-Oriented Programming

The application uses classes to represent people, users, projects, and tasks.

- Person: Represents a person using their name and email address.
- User: Inherits from "Person" and represents a registered user.
- Project: Represents a project and contains its tasks.
- Task: Represents a task, including its title, assigned user, and completion status.

These classes help organise related data and behaviour into reusable components. The project can also use properties, setters, class attributes, and object relationships to support validation and management.

Data Storage

Project information is stored in "data/projects.json".

The storage utility uses Python's "json" module to load existing data and save updated information. This allows information to persist between application runs. Missing or malformed JSON files should be handled without causing the application to crash unexpectedly.

Testing

Automated tests are located in the "tests/" directory.

The tests should verify:

- Creating users, projects, and tasks.
- Inheritance and object relationships.
- Adding tasks to projects and marking tasks as complete.
- Correct handling of task status and assigned users.
- Saving and loading JSON data.
- Handling missing or malformed JSON files.
- Important error conditions and invalid inputs.

Run the tests with Python's built-in "unittest" framework:

python -m unittest discover -s tests -v

The command runs the discovered tests and displays their results. A successful test run should report no failures or errors.

Debugging and Error Handling

The application should provide clear error messages for invalid commands, missing records, and data-storage problems. Testing and debugging help identify errors and confirm that the application behaves as expected.

Known Limitations

- Data is stored locally in a JSON file rather than a database.
- The application is designed for terminal use.
- Additional validation and automated tests may be needed to cover every possible invalid input.

Future Improvements

- Add commands for editing and deleting projects and tasks.
- Improve date and input validation.
- Add task searching and filtering.
- Expand automated test coverage.

License

This project was developed for educational purposes as part of a Python programming assignment.