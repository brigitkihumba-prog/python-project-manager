
from models.person import Person



class User(Person):

    user_count = 0


    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []
        User.user_count += 1


    def add_project(self, project):
        self.projects.append(project)


    def __str__(self):
        return f"{self.name} - {len(self.projects)} project(s)"