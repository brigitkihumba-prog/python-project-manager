
class Task:
    
    task_count = 0

    
    def __init__(self, title, assigned_to="Unassigned"):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to
        Task.task_count += 1

    
    @property
    def title(self):
        return self._title

    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Task title cannot be empty.")
        self._title = value.strip()

    
    def complete(self):
        self.status = "Complete"

    
    def __str__(self):
        return f"{self.title} - {self.status} ({self.assigned_to})"