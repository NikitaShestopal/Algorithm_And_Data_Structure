BOOK_CAPACITY = 10007  # Просте число для ефективного хешування

def hash_function(author, title):
    return (hash(author) + hash(title)) % BOOK_CAPACITY

class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(BOOK_CAPACITY)]

    def insert(self, author, title):
        index = hash_function(author, title)
        if (author, title) not in self.table[index]:
            self.table[index].append((author, title))

    def search(self, author, title):
        index = hash_function(author, title)
        return (author, title) in self.table[index]

    def remove(self, author, title):
        index = hash_function(author, title)
        if (author, title) in self.table[index]:
            self.table[index].remove((author, title))
