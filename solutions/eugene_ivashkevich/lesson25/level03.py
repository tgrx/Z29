from solutions.eugene_ivashkevich.lesson25.level02 import User as MetaUser


class User(MetaUser):
    def __eq__(self, other):
        if isinstance(other, User):
            return self.email == other.email
        return False
