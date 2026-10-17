# Represents a task belonging to a project
class Task:
    # Shared class attribute for counting tasks
    task_count = 0

    # Creates a task with a title and assigned user
    def __init__(self, title, assigned_to="Unassigned"):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to
        Task.task_count += 1

    # Gets the task title
    @property
    def title(self):
        return self._title

    # Checks the title before saving it
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Task title cannot be empty.")
        self._title = value.strip()

    # Marks the task as complete
    def complete(self):
        self.status = "Complete"

    # Returns a readable task description
    def __str__(self):
        return f"{self.title} - {self.status} ({self.assigned_to})"