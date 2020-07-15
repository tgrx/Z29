class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def find(self, begin):
        return sum(_c.startswith(begin) for _c in self.contacts)
