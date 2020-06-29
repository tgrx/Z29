from .level01 import User


class User(User):
    def __init__(self, name, email):
        self.name = name
        self.email = email
