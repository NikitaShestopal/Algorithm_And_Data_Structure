BOOK_CAPACITY = 100000007

def hash_function(author, title):
    return (hash(author) + hash(title)) % BOOK_CAPACITY

class HashTable:
    def __init__(self):
        self.table = [None] * BOOK_CAPACITY

    def insert(self, author, title):
        index = hash_function(author, title)
        while self.table[index] is not None:
            if self.table[index] == (author, title):
                return
            index = (index + 1) % BOOK_CAPACITY
        self.table[index] = (author, title)

    def search(self, author, title):
        index = hash_function(author, title)
        while self.table[index] is not None:
            if self.table[index] == (author, title):
                return True
            index = (index + 1) % BOOK_CAPACITY
        return False

    def remove(self, author, title):
        index = hash_function(author, title)
        while self.table[index] is not None:
            if self.table[index] == (author, title):
                self.table[index] = None
                return
            index = (index + 1) % BOOK_CAPACITY

hash_table = HashTable()
author_books = {}

