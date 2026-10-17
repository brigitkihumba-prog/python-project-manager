class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()


    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Please enter a valid email address.")
        self._email = value.strip()


    def __str__(self):
        return f"{self.name} ({self.email})"