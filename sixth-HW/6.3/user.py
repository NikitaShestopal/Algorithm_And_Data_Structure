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

def init():
    global hash_table, author_books
    hash_table = HashTable()
    author_books = {}

def addBook(author, title):
    hash_table.insert(author, title)
    if author not in author_books:
        author_books[author] = []
    author_books[author].append(title)
    author_books[author].sort()

def find(author, title):
    return hash_table.search(author, title)

def delete(author, title):
    hash_table.remove(author, title)
    if author in author_books and title in author_books[author]:
        author_books[author].remove(title)

def findByAuthor(author):
    return author_books.get(author, [])
