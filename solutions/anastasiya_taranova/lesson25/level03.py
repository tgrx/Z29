from solutions.anastasiya_taranova.lesson25.level02 import User as metametauser


class User(metametauser):
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.email == other.email
