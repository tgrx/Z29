from solutions.masha_gul.lesson25.level01 import User as UserParent


class User(UserParent):
    def __init__(self, name, email):
        self.name = name
        self.email = email
