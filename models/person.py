# Represents a person in the project management system
class Person:
    # Creates a person with a name and email
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Gets the person's name
    @property
    def name(self):
        return self._name

    # Checks the name before saving it
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    # Gets the person's email
    @property
    def email(self):
        return self._email

    # Checks the email before saving it
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Please enter a valid email address.")
        self._email = value.strip()

    # Returns a readable description of the person
    def __str__(self):
        return f"{self.name} ({self.email})"