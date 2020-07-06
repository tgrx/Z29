from solutions.alexander_sidorov.lesson25 import level02


class User(level02.User):
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.email == other.email
