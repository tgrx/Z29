from solutions.sergey_kasperovich.lesson25.level01 import User as UserValue


class User(UserValue):
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
