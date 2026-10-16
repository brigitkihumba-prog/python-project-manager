class Person:
    # Represent a person in the project management system. 

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def __str__(self):
    # return a string representation of the person in the format "Name <email>".
        return f"{self.name} <{self.email}>"