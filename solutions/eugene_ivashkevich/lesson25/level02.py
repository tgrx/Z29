from solutions.eugene_ivashkevich.lesson25.level01 import User as NewUser


class User(NewUser):
    def __init__(self, name, email):
        self.name = name
        self.email = email
