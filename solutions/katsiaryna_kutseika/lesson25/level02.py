from solutions.katsiaryna_kutseika.lesson25.level01 import User as MetaUser


class User(MetaUser):
    def __init__(self, name, email):
        self.name = name
        self.email = email
