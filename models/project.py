# Import date tools for checking project due dates
from datetime import date


# Represents a project that contains tasks
class Project:
    # Shared class attribute for counting projects
    project_count = 0

    # Creates a project with its details
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project.project_count += 1

    # Gets the project title
    @property
    def title(self):
        return self._title

    # Checks the title before saving it
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Project title cannot be empty.")
        self._title = value.strip()

    # Adds a task to this project
    def add_task(self, task):
        self.tasks.append(task)

    # Returns the project's title and task count
    def __str__(self):
        return f"{self.title} - {len(self.tasks)} task(s)"