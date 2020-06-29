from solutions.anastasiya_taranova.lesson25.level01 import User as user


class User(user):
    def __init__(self, name, email):
        self.name = name
        self.email = email
