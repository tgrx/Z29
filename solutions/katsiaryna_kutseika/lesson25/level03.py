from solutions.katsiaryna_kutseika.lesson25.level02 import User as User02


class User(User02):
    def __eq__(self, other):
        if isinstance(other, User):
            return self.email == other.email
        return False
