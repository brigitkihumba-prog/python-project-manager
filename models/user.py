# Import Person so User can inherit its features
from models.person import Person


# Represents a user in the project management system
class User(Person):
    # Shared class attribute for counting created users
    user_count = 0

    # Creates a user with a name and email
    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []
        User.user_count += 1

    # Adds a project to this user's list
    def add_project(self, project):
        self.projects.append(project)

    # Returns the user's name and project count
    def __str__(self):
        return f"{self.name} - {len(self.projects)} project(s)"