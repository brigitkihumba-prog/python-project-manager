# Import the person class from person.py
from models.person import Person

# Represent a user in the project management system. A user is a person who can create and manage projects and tasks.
class User(Person):

# Create a new user with the given name, email.    
    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []  # List of projects created by the user

# Add a project to the user's list of projects
    def add_project(self, project):
        self.projects.append(project)        

#Returns the user's name and number of projects.
    def __str__(self):
        return f"{self.name} - {len(self.projects)} project(s)"