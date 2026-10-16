#Represent a project that contains tasks
from datetime import date

class Project:
    # Create a new project with the given details.
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []  

    # Add a task to the project.
    def add_task(self, task):
        self.tasks.append(task)

    # Returns the project's title and task count.
    def __str__(self):
        return f"{self.title} - {len(self.tasks)} task(s))"