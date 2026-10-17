
from datetime import date



class Project:

    project_count = 0

 
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project.project_count += 1


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Project title cannot be empty.")
        self._title = value.strip()


    def add_task(self, task):
        self.tasks.append(task)


    def __str__(self):
        return f"{self.title} - {len(self.tasks)} task(s)"