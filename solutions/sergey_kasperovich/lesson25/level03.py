from solutions.sergey_kasperovich.lesson25.level02 import User as UserValue


class User(UserValue):
    def __eq__(self, other):
        return isinstance(other, User) and self.email == other.email
