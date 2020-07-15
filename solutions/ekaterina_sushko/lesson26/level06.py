class ContactBook:
    def __init__(self):
        self._book = []

    def add(self, contact):
        self._book.append(contact)

    def find(self, word):
        count = 0
        for i in self._book:
            if i.startswith(word):
                count += 1
        return count
