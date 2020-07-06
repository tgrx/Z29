from solutions.masha_gul.lesson25.level02 import User as UserParent


class User(UserParent):
    def __eq__(self, other):

        return isinstance(other, User) and self.email == other.email
