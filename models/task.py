# Represent a task belonging to a project.
class Task:

#Creates a task with a title and assigned user.    
    def __init__(self, title, assigned_to="Unassigned"):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

# Mark the task as completed.
    def complete(self):
        self.status = "Completed"        

# Returns a readable description of the task, including its title and status.
    def __str__(self):
        return f"{self.title} - {self.status} )({self.assigned_to})"